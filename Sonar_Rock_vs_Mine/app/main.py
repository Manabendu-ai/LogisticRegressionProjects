from fastapi import FastAPI
import joblib
from schemas import Sonar

app = FastAPI()

model = joblib.load("../model/sonar_model.pkl")

@app.get('/', tags=["prediction"])
def home():
    return {
        "data" : "Logistic Regression Model For Sonar Rock vs Mine Prediction"
    }

@app.post("/predict", tags=["prediction"])
def make_prediction(data : Sonar):
    prediction = model.predict([data.features])

    if prediction[0] == "R":
        result = "Rock"
    else:
        result = "Mine"

    return {
        "prediction" : result
    }