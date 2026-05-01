# 💳 Financial Fraud Detection System

An end-to-end Machine Learning project to detect fraudulent financial transactions using **XGBoost**, **FastAPI**, and **Streamlit**.

---

## 🚀 Overview

This project predicts whether a transaction is **Fraudulent** or **Normal** based on transaction data.

It includes:
- Machine Learning model (XGBoost)
- FastAPI backend for real-time prediction
- Streamlit dashboard for user interaction

---

## 🧠 Problem Statement

Financial fraud detection is difficult due to:

- Highly imbalanced dataset
- Very few fraud cases
- Need for accurate and real-time detection

This system is designed to:
- Detect fraud efficiently
- Reduce false positives
- Work in real-time using API

---

## 🏗️ System Architecture
CSV Data → Preprocessing → ML Model (XGBoost)
↓
FastAPI Backend
↓
Streamlit Dashboard


---

## 📊 Dataset

- Dataset: Credit Card Transactions
- Features:
  - V1 to V28 (PCA transformed features)
  - Amount (transaction value)
  - Class (Target variable)

Target:
- 0 → Normal
- 1 → Fraud

---

## ⚙️ Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Joblib

---

## 🔄 Workflow

1. Load dataset using Pandas  
2. Preprocess data (scaling Amount column)  
3. Split into training and testing data  
4. Train model using XGBoost  
5. Evaluate model performance  
6. Save model using Joblib  
7. Create API using FastAPI  
8. Build dashboard using Streamlit  

---

## 🧪 Model Details

- Algorithm: XGBoost Classifier  
- Handles imbalanced data using `scale_pos_weight`  
- Key Parameters:
  - n_estimators = 300  
  - max_depth = 6  
  - learning_rate = 0.1  

---

## 🔌 API Endpoints

### 1️⃣ Home Endpoint

GET /

Response:
{
"message": "API Running"
}

---

### 2️⃣ Predict Endpoint
POST /predict


### Sample Input

### Sample Input
{
"V1": 0.0,
"V2": 0.0,
"V3": 0.0,
"V4": 0.0,
"V5": 0.0,
"V6": 0.0,
"V7": 0.0,
"V8": 0.0,
"V9": 0.0,
"V10": 0.0,
"V11": 0.0,
"V12": 0.0,
"V13": 0.0,
"V14": 0.0,
"V15": 0.0,
"V16": 0.0,
"V17": 0.0,
"V18": 0.0,
"V19": 0.0,
"V20": 0.0,
"V21": 0.0,
"V22": 0.0,
"V23": 0.0,
"V24": 0.0,
"V25": 0.0,
"V26": 0.0,
"V27": 0.0,
"V28": 0.0,
"Amount": 149.62
}

### Sample Output
{
"prediction": 0,
"probability": 0.00001,
"result": "Normal"
}

---

## 💻 How to Run Locally

### 1. Clone Repository

git clone https://github.com/anup1203/fraud-detection-system.git

cd fraud-detection-system


---

### 2. Install Dependencies
pip install -r requirements.txt

---

### 3. Train Model
---
python train_model.py

### 4. Run FastAPI Server
uvicorn api:app --reload


Open in browser: http://127.0.0.1:8000/docs


---

### 5. Run Streamlit App

streamlit run app.py


---

## 📈 Features

- Real-time fraud detection  
- Machine learning-based predictions  
- API integration  
- CSV file upload  
- Interactive dashboard  
- Downloadable results  

---

## ⚠️ Limitations

- Dataset is highly imbalanced  
- Row-by-row API calls are slow  
- Free deployment may have cold start delay  

---

## 🔮 Future Improvements

- Batch prediction (faster processing)  
- Deep learning models  
- Real-time streaming system  
- Cloud optimization  

---

## 👨‍💻 Author

**Anup Yadav**  
GitHub: https://github.com/anup1203  

---

## ⭐ Project Status

✅ Completed  
🚀 Ready for interviews and demonstration  

---

## 📢 Interview Explanation

"I built an end-to-end fraud detection system using XGBoost for machine learning, FastAPI for backend APIs, and Streamlit for the frontend dashboard. The system handles imbalanced data and provides real-time fraud predictions."
