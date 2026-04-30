from crewai import Task, Crew
import logging

from agents.data_agent import data_agent
from agents.feature_agent import feature_agent
from agents.prediction_agent import prediction_agent
from agents.explanation_agent import explanation_agent

logging.basicConfig(filename='logs/system.log', level=logging.INFO)

def run_system(input_data):

    task1 = Task(
        description=f"Clean this patient data: {input_data}",
        agent=data_agent,
        expected_output="Cleaned patient data as dictionary"
    )

    task2 = Task(
        description="Convert cleaned data into features for ML model",
        agent=feature_agent,
        expected_output="Feature list for ML model"
    )

    task3 = Task(
        description="Predict heart disease using ML model",
        agent=prediction_agent,
        expected_output="Prediction result (0 or 1)"
    )

    task4 = Task(
        description="Explain the prediction result in simple terms",
        agent=explanation_agent,
        expected_output="Human readable explanation"
    )

    crew = Crew(
        agents=[data_agent, feature_agent, prediction_agent, explanation_agent],
        tasks=[task1, task2, task3, task4],
        verbose=True
    )

    result = crew.kickoff(inputs={"input_data": input_data})

    logging.info(result)

    return result


# test run
if __name__ == "__main__":
    sample_input = {
        "age": 52,
        "sex": 1,
        "cp": 2,
        "trestbps": 130,
        "chol": 250,
        "fbs": 0,
        "restecg": 1,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 1.2,
        "slope": 2,
        "ca": 0,
        "thal": 2
    }

    output = run_system(sample_input)
    print(output)