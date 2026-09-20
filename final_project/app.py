import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and expected columns
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction by krish❤️")
st.markdown("Provide the following details to check your heart stroke risk:")

# Collect user input
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)",80,200,120)
cholesterol = st.number_input("Cholesterol (mg/dL)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
resting_ecg = st.selectbox("Resting ECG",["Normal","ST","LVH"])
Max_hr = st.slider("Max Heart Rate",60,220,150)
exercise_angina = st.selectbox("Exercise-Induced Angina",["Y","N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0,6.0,1.0)
