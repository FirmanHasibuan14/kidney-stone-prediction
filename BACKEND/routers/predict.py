from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.predict import PredictionRequest, PredictionResponse, PredictionHistory
from services.ml_service import ml_service
from crud.predict import create_prediction, get_predictions
from typing import List

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_kidney_stone(request_data: PredictionRequest, db: Session = Depends(get_db)):
    try:
        result = ml_service.predict(request_data)
        prediction = result['prediction']
        probability = result['probability']

        history_data = {
            **request_data.dict(),
            'target': prediction,
            'probability': probability,
        }
        prediction_history = PredictionHistory(**history_data)
        await create_prediction(db, prediction_history)

        return {"prediction": prediction, "probability": probability}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[PredictionHistory])
async def get_prediction_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await get_predictions(db, skip, limit)