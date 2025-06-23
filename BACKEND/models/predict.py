from sqlalchemy import Column, Integer, Float, DateTime, String
from datetime import datetime
from database.connection import Base

class PredictionHistory(Base):
    __tablename__ = "prediction_history"
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    gravity = Column(Float)
    ph = Column(Float)
    osmo = Column(Integer)
    cond = Column(Float)
    urea = Column(Integer)
    calc = Column(Float)

    urine_volume = Column(Float)
    specific_gravity_calcium_ratio = Column(Float)
    calcium_conductivity_ratio = Column(Float)
    calcium_pH_interaction = Column(Float)
    urea_pH_interaction = Column(Float)
    osmolarity_calcium_interaction = Column(Float)

    target = Column(Integer)
    probability = Column(Float)
