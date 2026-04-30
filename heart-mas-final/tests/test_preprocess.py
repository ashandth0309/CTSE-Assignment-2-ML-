from tools.preprocess_tool import preprocess

def test_preprocess_valid():
    data = {"age": "50", "chol": "200"}
    result = preprocess(data)
    
    assert isinstance(result["age"], float)
    assert isinstance(result["chol"], float)


def test_preprocess_values():
    data = {"age": "60"}
    result = preprocess(data)
    
    assert result["age"] == 60.0