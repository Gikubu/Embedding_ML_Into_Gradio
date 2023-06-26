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
