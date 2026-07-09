import pandas as pd
import joblib

loaded = joblib.load("../model/titan.pkl")
model = loaded["model"]
feature_names = loaded["feature_names"]

def make_prediction(features):
    df = pd.DataFrame([features], columns=feature_names)
    return model.predict(df)
