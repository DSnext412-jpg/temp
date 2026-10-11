import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram

df = pd.DataFrame({
    "Product": ["A","B","C","D","F"],
    "Price": [20,25,80,75,100],
    "Rating": [4.2,4.5,4.8,4.7,4.9],
    "Sales": [500,650,1200,1100,1500]
})

X = StandardScaler().fit_transform(df[["Price","Rating","Sales"]])
Z = linkage(X, method='ward')

dendrogram(Z, labels=df["Product"].values)
plt.title("Dendrogram")
plt.show()