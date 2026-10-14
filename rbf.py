from sklearn import svm

X=[[1,2],[2,3],[5,5]]
y=[0,0,1]

model=svm.SVC(kernel="rbf")
model.fit(X,y)

print("Prediction:",model.predict([[4,4]]))




"""
A non-linear Support Vector Machine (SVM) is a machine 
learning classification algorithm that separates data into
different classes when a single straight line or flat plane 
cannot divide them
"""