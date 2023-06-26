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