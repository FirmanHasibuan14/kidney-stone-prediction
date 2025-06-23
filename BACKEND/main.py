from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Kidney Stone Prediction API. Go to /docs for documentation."}