import streamlit as st

from tools.preprocess_tool import preprocess
from tools.feature_tool import to_features
from tools.prediction_tool import predict
from tools.explanation_tool import explain

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Prediction System")

st.write("Enter patient details below:")

# Input fields
age = st.number_input("Age", 1, 120, 52)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
cp = st.number_input("Chest Pain Type (0-3)", 0, 3, 2)
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 130)
chol = st.number_input("Cholesterol", 100, 600, 250)
fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [1, 0])
restecg = st.number_input("Rest ECG (0-2)", 0, 2, 1)
thalach = st.number_input("Max Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Angina (1=Yes, 0=No)", [1, 0])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.2)
slope = st.number_input("Slope (0-2)", 0, 2, 2)
ca = st.number_input("Number of Major Vessels (0-3)", 0, 3, 0)
thal = st.number_input("Thal (1-3)", 1, 3, 2)

# Predict button
if st.button("Predict"):

    input_data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    # Pipeline (Agents simulation)
    cleaned = preprocess.run(input_data)
    features = to_features.run(cleaned)
    prediction = predict.run(features)
    result = explain.run(prediction)

    st.subheader("Result:")
    st.success(result)