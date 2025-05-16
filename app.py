import streamlit as st
import pandas as pd
import joblib
import sys
import os

# Add project root directory to Python path so 'src' is importable
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.preprocess import apply_feature_engineering
from src.config import MODEL_PATH
from src.utils import log_predictions

st.title("🔍 Fraud Transaction Detection App")

uploaded_file = st.file_uploader("Upload a CSV or Pickle file", type=["csv", "pkl"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".pkl"):
            data = pd.read_pickle(uploaded_file)
        else:
            st.error("Unsupported file format.")
            st.stop()

        # Validate required columns
        required_cols = [
            'TRANSACTION_ID', 'TX_DATETIME', 'CUSTOMER_ID', 
            'TERMINAL_ID', 'TX_AMOUNT', 'TX_TIME_SECONDS', 'TX_TIME_DAYS'
        ]
        missing_cols = [col for col in required_cols if col not in data.columns]
        if missing_cols:
            st.error(f"Missing required columns: {missing_cols}")
            st.stop()

        st.subheader("📄 Preview of Uploaded Data")
        st.write(data.head())

        # Apply preprocessing steps
        processed = apply_feature_engineering(data)

        # Load the trained model
        model = joblib.load(MODEL_PATH)

        # Generate predictions
        preds = model.predict(processed)
        data["Predicted_Fraud"] = preds

        # Log predictions
        log_predictions(data)

        st.subheader("✅ Predictions")
        st.write(data[["TRANSACTION_ID", "Predicted_Fraud"]].head())

        fraud_count = data["Predicted_Fraud"].sum()
        st.success(f"Detected {fraud_count} fraudulent transactions.")

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
