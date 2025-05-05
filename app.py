import streamlit as st
import pandas as pd
import joblib

# Change the page config
st.set_page_config(
    page_title="Premium App",       # This changes the browser tab title
    page_icon="💰",                 # You can use an emoji or path to an image
    layout="centered"
)

# Load trained model
model = joblib.load('best_rf_model.pkl')

st.title("Premium Price Prediction App")

st.write("Enter the following patient details:")

# Input fields for each feature
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

# Predict when button is clicked
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
    st.success(f"Estimated Premium Price: {prediction:,.2f}")
