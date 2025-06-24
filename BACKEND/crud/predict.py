from models.predict import PredictionHistory
from schemas.predict import PredictionHistoryBase
from sqlalchemy.orm import Session

def create_prediction(db: Session, prediction: dict):
    db_entry = PredictionHistory(**prediction)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_predictions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PredictionHistory).offset(skip).limit(limit).all()
