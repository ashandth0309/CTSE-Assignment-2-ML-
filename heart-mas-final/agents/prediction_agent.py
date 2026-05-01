from crewai import Agent
from tools.prediction_tool import predict

prediction_agent = Agent(
    role="Prediction Specialist",
    goal="Predict heart disease using ML model",
    backstory="Expert in machine learning predictions",
    tools=[predict],
    verbose=True,
    llm = "ollama/llama3"
)