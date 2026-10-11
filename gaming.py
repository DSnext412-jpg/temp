import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df=pd.read_csv("gaming_data.csv")
print(df.head())

df["player_type"] = df["player_type"].map({"Casual":0, "Professional":1})
x=df[["daily_play_time","achievements","purchases","gaming_level"]].values
y=df["player_type"].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print("\nLogistic Regression Results")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test,y_pred,target_names=["Casual","Professional"]))

new=scaler.transform([[5,55,18,50]])
print("\nPrediction for [5,55,18,50]:","Professional Gamer"if model.predict(new)[0]==1 else "Casual Gamer")

plt.figure(figsize=(6,4))
plt.bar(["Logistic Regression","Random Guess"],[accuracy_score(y_test, y_pred), 0.5], color=["green","red"])
plt.title("Model Comparison (Accuracy)"); 
plt.ylabel("Accuracy"); plt.ylim(0,1); plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["daily_play_time"], df["gaming_level"],c=y,cmap="coolwarm")
plt.title("Online Gaming Dataset"); 
plt.xlabel("Daily Play Time"); 

plt.ylabel("Gaming Level")
plt.colorbar(label="0=Casual, 1=Professional"); 
plt.show()