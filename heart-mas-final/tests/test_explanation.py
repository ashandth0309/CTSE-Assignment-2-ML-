from tools.explanation_tool import explain

def test_explanation_high():
    result = explain(1)
    assert "High" in result


def test_explanation_low():
    result = explain(0)
    assert "Low" in result