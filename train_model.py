# Student Performance Prediction System :-

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor

url = "https://drive.google.com/file/d/1w_dXCvxTbDF9l4Ue-XUPEodBlZQ0r9Os/view?usp=sharing"

df = pd.read_csv(url)

df = df.dropna(subset=['Gender','Result', 'Extra_Activities','Study_Hours', 'Attendance', 'Internet_Usage', 'Marks'])
df['Parental_Education'] = df['Parental_Education'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Study_Hours'] = df['Study_Hours'].fillna(df['Study_Hours'].mean())
df['Sleep_Hours'] = df['Sleep_Hours'].fillna(df['Sleep_Hours'].mean())
df['Internet_Usage'] = df['Internet_Usage'].replace(' ', np.nan)
df['Internet_Usage'] = df['Internet_Usage'].fillna(df['Internet_Usage'].mean())

le = LabelEncoder()

df['Result_Encoded'] = df['Result'].map({'Fail' : 0, 'Pass': 1})

df_copy = df.copy()

# print(scaled_df)
# print(minmaxscaled_df)

# Linear Regression - To get the 'Expected Marks' :-


# print(f"Expected Marks = {result1}")

def train_model1() : 

  X = df_copy[['Study_Hours', 'Attendance', 'Internet_Usage']]
  y = df_copy['Marks']

  model1 = RandomForestRegressor(n_estimators=100, random_state=42)

  model1.fit(X, y) 


  joblib.dump(model1, "model1.pkl")
  return model1

# Logisitic Regression - To Predict Pass/Fail (1/0) :-

def train_model2() :
   

  model2 = LogisticRegression()

  X2 = df[['Study_Hours', 'Attendance', 'Internet_Usage']]
  y2 = df['Result_Encoded']

  model2.fit(X2,y2)

  joblib.dump(model2, "model2.pkl")
  return model2


# result2 = round(model2.predict(values_df)[0],2)


print("Model trained and saved!")
