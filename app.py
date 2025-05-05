import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Set tab title and icon
st.set_page_config(
    page_title="Premium App",        # This sets the browser tab title
    page_icon="💰",                  # This sets the tab icon - you can also use a local file
    layout="centered"
)


# App title
st.title("Premium Price Prediction App")
st.markdown("Enter the following patient details:")

# Input fields
age = st.number_input("Age", min_value=0)
diabetes = st.selectbox("Diabetes", [0, 1])
bp_problems = st.selectbox("Blood Pressure Problems", [0, 1])
transplants = st.selectbox("Any Transplants", [0, 1])
chronic_diseases = st.selectbox("Any Chronic Diseases", [0, 1])
height = st.number_input("Height (cm)", min_value=0)
weight = st.number_input("Weight (kg)", min_value=0)
allergies = st.selectbox("Known Allergies", [0, 1])
cancer_history = st.selectbox("History of Cancer in Family", [0, 1])
surgeries = st.number_input("Number of Major Surgeries", min_value=0)

# Load model
model = joblib.load("best_rf_model.pkl")

# Predict
if st.button("Predict Premium Price"):
    input_df = pd.DataFrame([{
        'Age': age,
        'Diabetes': diabetes,
        'BloodPressureProblems': bp_problems,
        'AnyTransplants': transplants,
        'AnyChronicDiseases': chronic_diseases,
        'Height': height,
        'Weight': weight,
        'KnownAllergies': allergies,
        'HistoryOfCancerInFamily': cancer_history,
        'NumberOfMajorSurgeries': surgeries
    }])

    prediction = model.predict(input_df)[0]
    st.success(f" Estimated Premium Price: **KES {prediction:,.2f}**")
