# Importing the base libraries and packages
import pickle
import os
import pandas as pd
import gradio as gr
import re

# ----- Useful Lists
expected_inputs = ["gender", "SeniorCitizen", "Partner", "Dependents", "Contract", "tenure", "MonthlyCharges", "TotalCharges", "PaymentMethod", "PhoneService",
                   "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "PaperlessBilling"]
categoricals = ["gender", "SeniorCitizen", "Partner", "Dependents", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
                "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod"]
columns_to_scale = ["tenure", "MonthlyCharges", "TotalCharges"]


# ----- Helper Functions and Imports
# Function to load ML toolkit
def load_ml_toolkit(filepath=r"C:\Users\asus\Data_Analytics\linear_regression_model.pkl"):
    with open(filepath, "rb") as file:
        loaded_toolkit = pickle.load(file)
    return loaded_toolkit


# Importing the toolkit
loaded_toolkit = load_ml_toolkit()
encoder = loaded_toolkit["encoder"]
scaler = loaded_toolkit["scaler"]
model = loaded_toolkit["model"]


# Function to predict
def predict(*args, encoder = encoder, scaler = scaler, model = model):
    input_data = pd.DataFrame([args], columns= expected_inputs)
    input_data.fillna(0, inplace= True)
    
    encoder = loaded_toolkit["encoder"]
    scaler = loaded_toolkit["scaler"]
    model = loaded_toolkit["model"]

    # Encoding the categorical columns
    encoded_categoricals = encoder.transform(input_data[categoricals])
    encoded_categoricals = pd.DataFrame(encoded_categoricals, columns= encoder.get_feature_names_out().tolist())
    
    # Adding the categorical columns to the input dataframe
    df_encoded = input_data.join(encoded_categoricals)
    df_encoded.drop(columns= categoricals, inplace=True)
    
    # Scaling the numeric columns
    df_encoded[columns_to_scale] = scaler.transform(df_encoded[columns_to_scale])
    
    # Restricting column names to alpha-numeric characters
    df_processed = df_encoded.rename(columns= lambda x: re.sub("[^A-Za-z0-9_]+", "", x))
    
    # Making the prediction
    model_output = model.predict(df_processed)
    return float(model_output[0])