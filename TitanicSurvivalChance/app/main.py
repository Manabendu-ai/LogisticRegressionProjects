from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home():
    return {
        "Logistic Regression" : "Titan Survival Chance Prediction"
    }