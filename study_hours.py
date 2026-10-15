from sklearn.ensemble import RandomForestClassifier
X=[
    [2,60,55],
    [3,65,60],
    [4,70,65],
    [5,75,70],
    [6,80,75],
    [7,85,80],
    [1,55,50],
    [2,62,58],
    [5,78,72],
    [8,90,85]
]
y=[
    "Fail","Fail","Pass","Pass","Pass",
    "Pass","Fail","Fail","Pass","Pass"
  ]

model=RandomForestClassifier(n_estimators=10,random_state=42)
model.fit(X,y)
print("Prediction:", model.predict([[6,82,78]]))
print("Accuracy:", model.score(X,y))
