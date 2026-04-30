from crewai import Agent
from tools.preprocess_tool import preprocess

data_agent = Agent(
    role="Data Cleaning Specialist",
    goal="Clean patient data",
    backstory="Expert in medical data preprocessing",
    tools=[preprocess],   # now it's valid tool ✅
    verbose=True
)