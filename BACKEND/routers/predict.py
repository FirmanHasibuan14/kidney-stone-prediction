from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.connection import get_db
from schemas.predict import PredictionRequest, PredictionResponse, PredictionHistory
from services.ml_service import ml_service
from crud.predict import create_prediction, get_predictions

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict_kidney_stone(request: PredictionRequest, db: Session = Depends(get_db)):
    try:
        result = ml_service.predict(request)
        prediction = result["prediction"]
        probability = result["probability"]
        engineered_features = result["engineered_features"]

        history_data_to_save = {
            **request.dict(),
            **engineered_features,
            "target": prediction,
            "probability": probability
        }

        create_prediction(db=db, prediction=history_data_to_save)

        return PredictionResponse(
            target=prediction,
            probability=probability
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Terjadi kesalahan internal: {e}")

@router.get("/history", response_model=List[PredictionHistory])
def get_prediction_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_predictions(db, skip, limit)
