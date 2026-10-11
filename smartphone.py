import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

df=pd.read_csv("smartphone_data.csv")
df["price_category"]=df["price_category"].map({"low":0,"medium":1,"high":2})

X=df[["ram","storage","battery_capacity","camera_resolution"]].values
y=df["price_category"].values

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42, stratify=y)

scaler=StandardScaler()
x_train,x_test=scaler.fit_transform(x_train),scaler.transform(x_test)

model=LogisticRegression(max_iter=1000).fit(X_train, y_train)
y_pred=model.predict(X_test)

print("accuracy:",accuracy_score(y_test, y_pred))
print("F1 score:",f1_score(y_test,y_pred,average="weighted"))
print("confusion matrix:\n", confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["low","medium","high"]))

pred=model.predict(scaler.transform([[8,128,5000,50]]))[0]
print("Prediction for 8GB/128GB/5000mAh/50MP:", ["low Price","medium Price","high Price"][pred])

plt.bar(["Logistic Regression","Random Guess"],[accuracy_score(y_test, y_pred),0.33],color=["green","red"])
plt.title("Model Comparison"); plt.ylabel("Accuracy");
plt.show()

plt.scatter(df["ram"], df["storage"], c=y, cmap="coolwarm")
plt.title("smartphone dataset"); 
plt.xlabel("RAM"); 
plt.ylabel("storage")
plt.colorbar(label="0=low,1=medium,2=high"); 
plt.show()