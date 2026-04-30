from crewai.tools import tool

@tool
def explain(pred: int) -> str:
    """Explain prediction result in simple terms"""
    if pred == 1:
        return "High Risk ⚠️ – Consult doctor"
    else:
        return "Low Risk ✅ – Stay healthy"