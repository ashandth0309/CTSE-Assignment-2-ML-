from tools.prediction_tool import predict

def test_prediction_output():
    sample_features = [50,1,2,120,200,0,1,150,0,1.0,2,0,2]

    pred = predict(sample_features)

    assert pred in [0,1]