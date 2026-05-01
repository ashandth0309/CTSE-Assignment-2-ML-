from crewai import Agent
from tools.preprocess_tool import preprocess

data_agent = Agent(
    role="Data Cleaner",
    goal="Clean and validate patient input data",
    backstory="Expert in handling medical datasets",
    tools=[preprocess],
    verbose=True,
    llm = "ollama/llama3"
)