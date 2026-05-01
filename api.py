from fastapi import FastAPI
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# app create
app = FastAPI()

# model load
model = joblib.load("fraud_model.pkl")

# cleaning function
def clean_data(df):
    df = df.copy()
    df = df.dropna()

    if "Amount" in df.columns:
        scaler = StandardScaler()
        df["Amount"] = scaler.fit_transform(df[["Amount"]])

    return df


# home route
@app.get("/")
def home():
    return {"message": "NEW VERSION RUNNING"}   # test line


# predict route
@app.post("/predict")
def predict(data: dict):
    try:
        # convert input to dataframe
        df = pd.DataFrame([data])

        # clean
        df = clean_data(df)

        # prediction
        prediction = model.predict(df)

        # probability
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(df)[0][1]
        else:
            prob = 0.0

        return {
            "prediction": int(prediction[0]),
            "probability": float(prob),
            "result": "Fraud" if prediction[0] == 1 else "Normal"
        }

    except Exception as e:
        return {"error": str(e)}