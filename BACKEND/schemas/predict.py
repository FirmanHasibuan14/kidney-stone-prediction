from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PredictionRequest(BaseModel):
    gravity: float
    ph: float
    osmo: int
    cond: float
    urea: int
    calc: float

class PredictionResponse(BaseModel):
    target: int
    probability: int

class PredictionHistoryBase(PredictionRequest):
    target: int
    probability: float
    urine_volume: float
    specific_gravity_calcium_ratio: float
    calcium_conductivity_ratio: float
    calcium_pH_interaction: float
    urea_pH_interaction: float
    osmolarity_calcium_interaction: float

class PredictionHistory(PredictionHistoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True