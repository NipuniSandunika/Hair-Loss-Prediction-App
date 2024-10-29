import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained decision tree model
pickle_in = open("best_dt_model.pkl", "rb")
best_dt_model = pickle.load(pickle_in)

def predict_hair_loss(features):
    """Function to predict hair loss using the decision tree model."""
    prediction = best_dt_model.predict([features])
    return prediction[0]

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
    Medical_Conditions =  st.selectbox("Medical Conditions", options=['Eczema', 'Dermatosis', 'Ringworm', 'Psoriasis', 'Alopecia Areata ','Scalp Infection', 'Seborrheic Dermatitis', 'Dermatitis', 'Thyroid Problems','Androgenetic Alopecia'])
    Medications_Treatments = st.selectbox("Medications & Treatments", options=['Antibiotics', 'Antifungal Cream', 'Accutane', 'Chemotherapy','Steroids', 'Rogaine', 'Blood Pressure Medication', 'Immunomodulators','Antidepressants ', 'Heart Medication '])
    Nutritional_Deficiencies =  st.selectbox("Nutritional Deficiencies", options=['Magnesium deficiency', 'Protein deficiency', 'Biotin Deficiency ','Iron deficiency', 'Selenium deficiency', 'Omega-3 fatty acids','Zinc Deficiency','Vitamin A Deficiency', 'Vitamin D Deficiency', 'Vitamin E deficiency'])

    # Include all features in the mapping
    binary_map = {"No": 0, "Yes": 1}
    stress_map = {"Low": 1, "Moderate": 2, "High": 3}
    Medical_Conditions_map = {'Eczema':1, 'Dermatosis':2, 'Ringworm':3, 'Psoriasis':4, 'Alopecia Areata':5, 'Scalp Infection':6, 'Seborrheic Dermatitis':7, 'Dermatitis':8, 'Thyroid Problems':9,'Androgenetic Alopecia':10}
    Medications_Treatments_map = {'Antibiotics':1, 'Antifungal Cream':2, 'Accutane':3, 'Chemotherapy':4,'Steroids':5, 'Rogaine':6, 'Blood Pressure Medication':7, 'Immunomodulators':8, 'Antidepressants ':9, 'Heart Medication ':10}

    Nutritional_Deficiencies_map = {'Magnesium deficiency':1, 'Protein deficiency':2, 'Biotin Deficiency ':3,'Iron deficiency':4, 'Selenium deficiency':5, 'Omega-3 fatty acids':6,'Zinc Deficiency':7,'Vitamin A Deficiency':8, 'Vitamin D Deficiency':9, 'Vitamin E deficiency':10}

    # Apply the mapping for all features
    features = [binary_map[Genetics],
                binary_map[Hormonal_Changes], 
                binary_map[Poor_Hair_Care_Habits], 
                binary_map[Environmental_Factors], 
                binary_map[Smoking], 
        	binary_map[Weight_Loss],
        	Age, 
        	stress_map[Stress], 
        	Medical_Conditions_map[Medical_Conditions], 
        	Medications_Treatments_map[Medications_Treatments], 
        	Nutritional_Deficiencies_map[Nutritional_Deficiencies]]
    
    # When the 'Predict' button is clicked
    if st.button("Predict"):
        result = predict_hair_loss(features)
        st.success(f"The predicted hair loss status is: {'Hair Loss' if result == 1 else 'No Hair Loss'}")

if __name__ == '__main__':
    main()
