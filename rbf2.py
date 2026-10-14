from sklearn.neural_network import MLPRegressor

X=[[1],[2],[3],[4],[5]]
y=[2,4,6,8,10]
model=MLPRegressor(hidden_layer_sizes=(5,),max_iter=5000,random_state=1)
model.fit(X,y)

print("Prediction:",model.predict([[6]]))