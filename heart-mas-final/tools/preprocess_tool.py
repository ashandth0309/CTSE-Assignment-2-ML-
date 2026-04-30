from typing import Dict
from crewai.tools import tool

def preprocess(data: Dict) -> Dict:
    cleaned = {}
    for k, v in data.items():
        cleaned[k] = float(v)
    return cleaned

@tool
def preprocess(data: dict) -> dict:
    """Clean and convert input patient data into numeric format"""
    
    cleaned = {}
    for k, v in data.items():
        cleaned[k] = float(v)
    return cleaned