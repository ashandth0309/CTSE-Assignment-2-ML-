import logging

from tools.preprocess_tool import preprocess
from tools.feature_tool import to_features
from tools.prediction_tool import predict
from tools.explanation_tool import explain

logging.basicConfig(filename='logs/system.log', level=logging.INFO)

def run_system(input_data):

    print("\n--- Agent 1: Data Agent (Cleaning Data) ---")
    cleaned_data = preprocess.run(input_data)

    print("\n--- Agent 2: Feature Agent (Feature Extraction) ---")
    features = to_features.run(cleaned_data)

    print("\n--- Agent 3: Prediction Agent (ML Prediction) ---")
    prediction = predict.run(features)

    print("\n--- Agent 4: Explanation Agent (Generating Explanation) ---")
    result = explain.run(prediction)

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
    print("\nFinal Output:", output)