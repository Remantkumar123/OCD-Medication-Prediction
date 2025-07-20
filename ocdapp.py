import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("gaussian_naive_bayes_model.pkl")  # Make sure the path is correct

# Title
st.title("🧠 OCD Medication Prescriber")

st.write("Provide the following patient details to predict the most suitable medication:")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, step=1)

gender = st.selectbox("Gender", ["Male", "Female"])
gender_val = 1 if gender == "Male" else 0

duration = st.number_input("Duration of Symptoms (months)", min_value=0.0, step=0.1)

previous_diagnosis = st.selectbox("Previous Diagnoses", [0, 1])

obsessions_score = st.slider("Y-BOCS Score (Obsessions)", 0, 20)
compulsions_score = st.slider("Y-BOCS Score (Compulsions)", 0, 20)

depression = st.selectbox("Depression Diagnosis", ["Yes", "No"])
depression_val = 1 if depression == "Yes" else 0

anxiety = st.selectbox("Anxiety Diagnosis", ["Yes", "No"])
anxiety_val = 1 if anxiety == "Yes" else 0

# Prediction button
if st.button("🔮 Predict Medication"):
    # Create input DataFrame
    input_data = pd.DataFrame([[age, gender_val, duration, previous_diagnosis,
                                obsessions_score, compulsions_score,
                                depression_val, anxiety_val]],
                              columns=['Age', 'Gender', 'Duration of Symptoms (months)',
                                       'Previous Diagnoses', 'Y-BOCS Score (Obsessions)',
                                       'Y-BOCS Score (Compulsions)', 'Depression Diagnosis',
                                       'Anxiety Diagnosis'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # if-elif to map numeric prediction to medication
    if prediction == 0:
        medication = "SNRI"
    elif prediction == 1:
        medication = "SSRI"
    elif prediction == 2:
        medication = "Benzodiazepine"
    elif prediction == 3:
        medication = "None"
    else:
        medication = "Unknown"

    # Display result
    st.success(f"✅ Predicted Medication: **{medication}**")

    if prediction == 0:
        medication = "SNRI"
        st.write("SNRIs, or serotonin-norepinephrine reuptake inhibitors, are a class of "
                 "antidepressant medications that work by increasing the levels of "
                 "serotonin and norepinephrine in the brain. These neurotransmitters "
                 "play a role in mood, energy, and focus. SNRIs are often used to treat"
                 " depression, anxiety disorders, and chronic pain conditions. ")
    elif prediction == 1:
        medication = "SSRI"
        st.write("SSRIs, or Selective Serotonin Reuptake Inhibitors, are a type of "
                 "antidepressant medication that increases serotonin levels in the brain "
                 "by preventing its reabsorption. They are commonly used to treat depression,"
                 " anxiety disorders, and other psychological conditions.")
    elif prediction == 2:
        medication = "Benzodiazepine"
        st.write("Benzodiazepines are a class of CNS depressant drugs, commonly known as benzos used to treat anxiety, "
                 "insomnia, and seizures. They work by enhancing the effects of the neurotransmitter"
                 " GABA in the brain, leading to sedative and anxiolytic effects. While effective,"
                 " they carry risks of side effects, potential for misuse and abuse, and the risk of "
                 "developing physical dependence, making them a controlled substance. ")
    elif prediction == 3:
        medication = "None"
        st.write("Whoa! Everything’s good with you — you’re doing great.")
    else:
        medication = "Unknown"
        st.write("Whoa! Everything’s good with you — you’re doing great.")

