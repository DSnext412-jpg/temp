import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2 
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA 
dataset=pd.read_csv("loan.csv") 
print("Original Loan Dataset:") 
print(dataset)

X=dataset.drop(columns=["Application_ID", "Loan_Status"]) 
y=dataset["Loan_Status"].map({ 
"Approved": 1, 
"Rejected": 0 
})

print("\nInput Features (X):") 
print(X) 
print("\nTarget (y):") 
print(y) 
print("A) FEATURE SELECTION") 
selector = SelectKBest(score_func=chi2, k=2) 
X_selected = selector.fit_transform(X, y) 
selected_features = X.columns[selector.get_support()] 

print("\nSelected Features:") 
print(list(selected_features)) 
print("\nSelected Feature Data:") 
print(X_selected) 
print("B) FEATURE EXTRACTION USING PCA") 

scaler=StandardScaler() 
X_scaled=scaler.fit_transform(X) 
print("\nStandardized Data:") 
print(X_scaled) 
pca=PCA(n_components=2) 
X_pca=pca.fit_transform(X_scaled) 

pca_data=pd.DataFrame( 
        X_pca, 
        columns=["Principal_Component_1", 
        "Principal_Component_2"] 
) 
 
pca_data["Loan_Status"] = dataset["Loan_Status"] 
print("\nPCA Reduced Dataset:") 
print(pca_data) 