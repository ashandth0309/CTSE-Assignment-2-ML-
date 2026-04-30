from crewai.tools import tool

@tool
def to_features(data: dict) -> list:
    """Convert cleaned data into feature list for ML model"""
    return [
        data["age"], data["sex"], data["cp"], data["trestbps"],
        data["chol"], data["fbs"], data["restecg"], data["thalach"],
        data["exang"], data["oldpeak"], data["slope"],
        data["ca"], data["thal"]
    ]