from crewai import Agent
from tools.explanation_tool import explain

explanation_agent = Agent(
    role="Medical Advisor",
    goal="Explain prediction results clearly",
    backstory="Doctor-like assistant for patient guidance",
    tools=[explain],
    verbose=True,
    llm = "ollama/llama3"
)