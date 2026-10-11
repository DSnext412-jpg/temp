import pandas as pd
from sklearn.preprocessing import LabelEncoder

df1=pd.DataFrame({"brand":["samsung","apple","onePlus","oppo","vivo"],
                    "model":["S24","iphone 18","oneplus 12r","oppo 10x","vivo V30"],
                    "price":[80000,70000,60000,25000,30000],
                    "RAM":[8,6,12,8,8]})

df2 = pd.DataFrame(
    {"model":["S24","iphone 18","oneplus 12r","oppo 10x","vivo V30"],
    "storage":[256,128,256,128,256],
    "battery capacity":[4000,3349,5400,5000,5000],
    "OS":["android","iOS","android","android","android"]}
    )

print("dataframe 1:\n",df1)
print("dataframe 2:\n",df2)

df=pd.merge(df1,df2,on="Model")
print("\nMerged DataFrame:\n",df)

df["brand encoded"]=LabelEncoder().fit_transform(df["brand"])
print("after label encoding:\n",df)

df = pd.get_dummies(df,columns=["OS"],dtype=int)
print("final transformed data frame: \n",df)