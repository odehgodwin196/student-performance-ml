import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("main/student_score_model.pkl")

st.title("Student Exam Score Predictor")

st.write("Enter student information to predict final exam score")

# Input features
G1 = st.number_input("First Period Grade (G1)", 0, 20)
G2 = st.number_input("Second Period Grade (G2)", 0, 20)
studytime = st.slider("Study Time (1–4)", 1, 4)
failures = st.slider("Past Failures", 0, 4)
absences = st.number_input("Number of Absences", 0, 50)
Medu = st.slider("Mother Education Level (0–4)", 0, 4)
Fedu = st.slider("Father Education Level (0–4)", 0, 4)
internet = st.selectbox("Internet Access", [0,1])
schoolsup = st.selectbox("School Support", [0,1])
famsup = st.selectbox("Family Support", [0,1])
sex_M = st.selectbox("Male (1) / Female (0)", [0,1])

# Predict
if st.button("Predict Score"):

    input_data = pd.DataFrame([[G1,G2,studytime,failures,absences,Medu,Fedu,schoolsup,famsup,internet,sex_M]],
    columns=['G1','G2','studytime','failures','absences','Medu','Fedu','schoolsup','famsup','internet','sex_M'])

    prediction = model.predict(input_data)

    st.success(f"Predicted Final Score (G3): {prediction[0]:.2f}")

if studytime < 2:
    st.warning("Recommendation: Increase study time to improve performance.")

if absences > 10:
    st.warning("Recommendation: Reduce absences for better academic results.")

if failures > 1:
    st.warning("Recommendation: Provide academic support to avoid repeated failures.")
