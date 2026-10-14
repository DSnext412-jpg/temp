from sklearn.cluster import KMeans 
from sklearn.linear_model import LogisticRegression 

X=[[2,40],[3,45],[8,85],[9,90]] 
y=[0,0,1,1] 

supervised=LogisticRegression()

supervised.fit(X,y)
print("supervised prediction for [7, 80]:",supervised.predict([[7,80]])[0])

unsupervised=KMeans(n_clusters=2,random_state=0)

unsupervised.fit(X)
print("unsupervised clusters:",unsupervised.labels_)