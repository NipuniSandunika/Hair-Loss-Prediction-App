import numpy as np
import pandas as pd
from joblib import load  
import streamlit as st

# Load the trained decision tree model
best_dt_model = load("best_dt_model.joblib")  # Use joblib to load the model

def predict_hair_loss(features):
    """Function to predict hair loss using the decision tree model."""
    
    # Debugging: Print the shape and types of features
    st.write("Input Features:", features)
    st.write("Feature Types:", [type(feature) for feature in features])
    
    try:
        prediction = best_dt_model.predict([features])
        return prediction[0]
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None  # Return None or a default value in case of error

def main():
    # HTML for styling
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">HAIR LOSS PREDICTOR</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Create input fields for each feature
    Genetics = st.selectbox("Genetics", options=["No", "Yes"])
    Hormonal_Changes = st.selectbox("Hormonal Changes", options=["No", "Yes"])
    Poor_Hair_Care_Habits = st.selectbox("Poor Hair Care Habits", options=["No", "Yes"])
    Environmental_Factors = st.selectbox("Environmental Factors", options=["No", "Yes"])
    Smoking = st.selectbox("Smoking", options=["No", "Yes"])
    Weight_Loss = st.selectbox("Weight Loss", options=["No", "Yes"])
    Age = st.number_input("Age", min_value=0, step=1)

    # Additional input fields
    Stress = st.selectbox("Stress Level", options=["Low", "Moderate", "High"])
    Medical_Conditions = st.selectbox("Medical Conditions", options=['No Data', 'Eczema', 'Dermatosis', 'Ringworm', 'Psoriasis', 'Alopecia Areata ',
                                                                   'Scalp Infection', 'Seborrheic Dermatitis', 'Dermatitis', 'Thyroid Problems',
                                                                   'Androgenetic Alopecia'])
    Medications_Treatments = st.selectbox("Medications & Treatments", options=['No Data', 'Antibiotics', 'Antifungal Cream', 'Accutane', 'Chemotherapy',
                                                                   'Steroids', 'Rogaine', 'Blood Pressure Medication', 'Immunomodulators',
                                                                   'Antidepressants ', 'Heart Medication '])
    Nutritional_Deficiencies = st.selectbox("Nutritional Deficiencies", options=['No Data', 'Magnesium deficiency', 'Protein deficiency', 'Biotin Deficiency ',
                                                                   'Iron deficiency', 'Selenium deficiency', 'Omega-3 fatty acids', 'Zinc Deficiency', 
                                                                   'Vitamin A Deficiency', 'Vitamin D Deficiency', 'Vitamin E deficiency'])

    # Include all features in the mapping
    binary_map = {"No": 0, "Yes": 1}
    stress_map = {"Low": 1, "Moderate": 2, "High": 3}
    Medical_Conditions_map = {'No Data': 1, 'Eczema': 2, 'Dermatosis': 3, 'Ringworm': 4, 'Psoriasis': 5, 'Alopecia Areata ': 6,
                              'Scalp Infection': 7, 'Seborrheic Dermatitis': 8, 'Dermatitis': 9, 'Thyroid Problems': 10,
                              'Androgenetic Alopecia': 11}
    Medications_Treatments_map = {'No Data': 1, 'Antibiotics': 2, 'Antifungal Cream': 3, 'Accutane': 4, 'Chemotherapy': 5,
                                   'Steroids': 6, 'Rogaine': 7, 'Blood Pressure Medication': 8, 'Immunomodulators': 9,
                                   'Antidepressants ': 10, 'Heart Medication ': 11}

    Nutritional_Deficiencies_map = {'No Data': 1, 'Magnesium deficiency': 2, 'Protein deficiency': 3, 'Biotin Deficiency ': 4,
                                     'Iron deficiency': 5, 'Selenium deficiency': 6, 'Omega-3 fatty acids': 7, 'Zinc Deficiency': 8, 
                                     'Vitamin A Deficiency': 9, 'Vitamin D Deficiency': 10, 'Vitamin E deficiency': 11}

    # Apply the mapping for all features
    features = [
        binary_map[Genetics], 
        binary_map[Hormonal_Changes], 
        binary_map[Poor_Hair_Care_Habits], 
        binary_map[Environmental_Factors], 
        binary_map[Smoking], 
        binary_map[Weight_Loss],
        Age, 
        stress_map[Stress], 
        Medical_Conditions_map[Medical_Conditions], 
        Medications_Treatments_map[Medications_Treatments], 
        Nutritional_Deficiencies_map[Nutritional_Deficiencies]
    ]
    
    # When the 'Predict' button is clicked
    if st.button("Predict"):
        result = predict_hair_loss(features)
        if result is not None:
            st.success(f"The predicted hair loss status is: {'Hair Loss' if result == 1 else 'No Hair Loss'}")

if __name__ == '__main__':
    main()
