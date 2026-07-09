from fastapi import FastAPI
from .router import titan
app = FastAPI()
app.include_router(titan.router)
@app.get('/')
def home():
    return {
        "Logistic Regression" : "Titan Survival Chance Prediction"
    }