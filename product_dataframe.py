import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data={
'Product_ID':[101,102,103,104,105],
'Price':[100,200,150,300,250],
'Quantity_Sold':[10,20,15,30,25],
'Discount':[5,10,0,15,20],
'Revenue':[950,3600,2250,7650,5000]
}
df=pd.DataFrame(data)
scaled_df=pd.DataFrame(MinMaxScaler().fit_transform(df), columns=df.columns)
print("Original:\n",df)
print("\nScaled:\n",scaled_df)