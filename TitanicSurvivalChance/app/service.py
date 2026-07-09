import pandas as pd
from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).parent.parent / "model" / "titan.pkl"

loaded = joblib.load(MODEL_PATH)
model = loaded["model"]
feature_names = loaded["feature_names"]

def make_prediction(features):
    df = pd.DataFrame([features], columns=feature_names)
    return model.predict(df)
