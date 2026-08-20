import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("dosage_predictor.pkl")

# Title and description
st.title("💉 Personalized Diabetes Medicine & Dosage Recommender")
st.write("Enter your health details below to predict your medicine dosage level and get personalized recommendations.")

# Input fields
Pregnancies = st.number_input("Pregnancies", 0, 20, step=1)
Glucose = st.slider("Glucose Level", 0, 300)
BloodPressure = st.slider("Blood Pressure", 0, 200)
SkinThickness = st.slider("Skin Thickness (mm)", 0, 100)
Insulin = st.slider("Insulin Level", 0, 900)
BMI = st.number_input("BMI", 0.0, 70.0, step=0.1)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, step=0.01)
Age = st.slider("Age", 1, 100)

# Predict button
if st.button("🔎 Predict Dosage"):
    # Prepare the input
    input_data = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                BMI, DiabetesPedigreeFunction, Age]],
                                columns=['Pregnancies', 'Glucose', 'BloodPressure',
                                         'SkinThickness', 'Insulin', 'BMI',
                                         'DiabetesPedigreeFunction', 'Age'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Map prediction
    dosage_map = {0: "Low", 1: "Medium", 2: "High"}
    predicted_label = dosage_map.get(prediction, "Unknown")

    # Recommended Metformin dosage based on prediction
    metformin_dosage = {
        "Low": "500",
        "Medium": "1000",
        "High": "1500"
    }
    predicted_dose = metformin_dosage.get(predicted_label, "N/A")

    # Show results
    st.success(f"🔔 Predicted Dosage Level: **{predicted_label}**")
    st.markdown(f"💊 **Recommended Metformin Dosage**: `{predicted_dose} mg/day`")

    # Show tips based on dosage level
    st.markdown("---")
    st.subheader("🩺 Health Tips & Suggestions")

    if predicted_label == "Low":
        st.info("✔️ Keep up the healthy habits.\n✔️ Maintain a balanced diet and exercise.\n✔️ Regular monitoring is still important.")
    elif predicted_label == "Medium":
        st.warning("⚠️ Consider reducing sugar and carb intake.\n⚠️ Follow moderate exercise routine.\n⚠️ Monitor blood sugar more frequently.")
    elif predicted_label == "High":
        st.error("❗ Your sugar level is high.\n❗ Follow strict medical guidance.\n❗ Regularly check blood glucose and consider insulin therapy if prescribed.")



