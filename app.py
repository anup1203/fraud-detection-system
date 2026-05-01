import streamlit as st
import joblib
import pandas as pd

model = joblib.load("fraud_model.pkl")

st.title("💳 Financial Fraud Detection System")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("📊 Data Preview:")
    st.write(df.head())

    if st.button("Predict Fraud"):
        X = df.drop('Class', axis=1, errors='ignore')

        predictions = model.predict(X)

        df['Prediction'] = predictions

        st.write("✅ Prediction Result:")
        st.write(df.head())

        fraud_count = sum(predictions)

        st.error(f"⚠️ Fraud Transactions: {fraud_count}")