from sklearn import svm

X=[[1,2],[2,3],[5,5]]
y=[0,0,1]

model=svm.SVC(kernel="rbf")
model.fit(X,y)

print("Prediction:",model.predict([[4,4]]))
