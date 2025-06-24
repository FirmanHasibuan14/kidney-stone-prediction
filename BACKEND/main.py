from fastapi import FastAPI
from routers import predict
from core.config import settings
from database.connection import create_tables

create_tables()

app = FastAPI(
    title = settings.APP_NAME,
    version = "1.0.0"
)

app.include_router(predict.router, prefix="/predict", tags=["Predict"])
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Kidney Stone Prediction API. Go to /docs for documentation."}