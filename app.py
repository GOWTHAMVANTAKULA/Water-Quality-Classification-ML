
import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier # Import CatBoostClassifier for loading the model

# Load the trained CatBoost model using its native load_model method
model = CatBoostClassifier() # Initialize an empty CatBoost model
model.load_model('catboost_model.cbm') # Load the trained model from the .cbm file

# Define the order of columns used during training
# Make sure this matches the order of 'parameters' list in your notebook, excluding 'Use Based Class'
feature_columns = [
    "Temperature", "pH", "Dissolved O2", "COD", "Nitrate N", "Amonia N",
    "Phosphate", "Fecal Coliform", "Total Coliform", "Turbidity",
    "Total Dissolved Solids", "Hardness CaCo3", "Chlorides", "Sulphate"
]

# Define the mapping for Use Based Class labels
# This should match the label encoding done during training
class_mapping = {
    0: 'A (Drinking Water source without conventional treatment but after disinfection)',
    1: 'B (Outdoor bathing(Organized))',
    2: 'C (Drinking water source)',
    3: 'E (Irrigation, industrial cooling and controlled waste)'
}

st.title("Water Quality Classification App")
st.write("Enter the water quality parameters to predict its use-based class.")

# Create input fields for each feature
input_data = {}
with st.sidebar:
    st.header("Water Quality Parameters")
    for col in feature_columns:
        if col in ["Temperature", "pH", "Dissolved O2", "Nitrate N", "Amonia N", "Phosphate", "Chlorides", "Sulphate"]:
            # Use more sensible default values for better testing
            if col == "Temperature": input_data[col] = st.number_input(f"Enter {col}", value=25.0, format="%.2f", min_value=0.0)
            elif col == "pH": input_data[col] = st.number_input(f"Enter {col}", value=7.5, format="%.2f", min_value=0.0)
            elif col == "Dissolved O2": input_data[col] = st.number_input(f"Enter {col}", value=6.0, format="%.2f", min_value=0.0)
            elif col == "Nitrate N": input_data[col] = st.number_input(f"Enter {col}", value=1.0, format="%.2f", min_value=0.0)
            elif col == "Amonia N": input_data[col] = st.number_input(f"Enter {col}", value=0.5, format="%.2f", min_value=0.0)
            elif col == "Phosphate": input_data[col] = st.number_input(f"Enter {col}", value=0.3, format="%.2f", min_value=0.0)
            elif col == "Chlorides": input_data[col] = st.number_input(f"Enter {col}", value=20.0, format="%.2f", min_value=0.0)
            elif col == "Sulphate": input_data[col] = st.number_input(f"Enter {col}", value=30.0, format="%.2f", min_value=0.0)
        elif col == "COD":
            input_data[col] = st.number_input(f"Enter {col}", value=15.0, format="%.2f", min_value=0.0)
        elif col == "Fecal Coliform": input_data[col] = st.number_input(f"Enter {col}", value=50.0, format="%.2f", min_value=0.0)
        elif col == "Total Coliform": input_data[col] = st.number_input(f"Enter {col}", value=200.0, format="%.2f", min_value=0.0)
        elif col == "Turbidity": input_data[col] = st.number_input(f"Enter {col}", value=2.0, format="%.2f", min_value=0.0)
        elif col == "Total Dissolved Solids": input_data[col] = st.number_input(f"Enter {col}", value=300.0, format="%.2f", min_value=0.0)
        elif col == "Hardness CaCo3": input_data[col] = st.number_input(f"Enter {col}", value=100.0, format="%.2f", min_value=0.0)


# Convert input data to DataFrame for prediction
input_df = pd.DataFrame([input_data])

# Display input data for debugging
st.subheader("Input Data for Prediction:") # Debugging line
st.dataframe(input_df) # Changed to st.dataframe for better display of DataFrame

if st.button("Predict Water Class"):
    prediction_proba = model.predict_proba(input_df)
    
    # Display prediction probabilities for debugging
    st.subheader("Prediction Probabilities:") # Debugging line
    st.write(prediction_proba) # Debugging line

    predicted_class_index = np.argmax(prediction_proba, axis=1)[0]
    predicted_class_label = class_mapping[predicted_class_index]

    st.subheader("Prediction:")
    st.write(f"The predicted water use-based class is: **{predicted_class_label}**")

    st.subheader("Probability Distribution:")
    proba_df = pd.DataFrame({"Class": list(class_mapping.values()), "Probability": prediction_proba[0]})
    st.bar_chart(proba_df.set_index("Class"))

st.sidebar.subheader("About the App")
st.sidebar.info(
    "This app uses a CatBoost Classifier model to predict the use-based class of water "
    "based on various water quality parameters. The model was trained on the provided dataset."
)
