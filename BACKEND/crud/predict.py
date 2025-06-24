from models.predict import PredictionHistory 
from schemas.predict import PredictionHistoryBase
from sqlalchemy.orm import Session

async def create_prediction(db: Session, prediction: PredictionHistoryBase):
    db_entry = PredictionHistory(**prediction.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

async def get_predictions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PredictionHistory).offset(skip).limit(limit).all()