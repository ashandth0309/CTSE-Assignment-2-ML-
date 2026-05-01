from crewai import Agent
from tools.feature_tool import to_features

feature_agent = Agent(
    role="Feature Engineer",
    goal="Convert patient data into ML features",
    backstory="Expert in feature engineering",
    tools=[to_features],
    verbose=True,
    llm = "ollama/llama3"
)