import pandas as pd
from xgboost import XGBClassifier
import joblib

df = pd.read_csv("creditcard.csv")

X = df.drop('Class', axis=1)
y = df['Class']

model = XGBClassifier(scale_pos_weight=577)
model.fit(X, y)

joblib.dump(model, "fraud_model.pkl")

print("Model trained and saved!")