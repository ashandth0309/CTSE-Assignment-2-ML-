from crewai.tools import tool
import joblib

model = joblib.load("model/model.pkl")

@tool
def predict(features: list) -> int:
    """Predict heart disease using trained model"""
    return int(model.predict([features])[0])