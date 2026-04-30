from main import run_system

def test_full_pipeline():

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

    result = run_system(sample_input)

    assert result is not None