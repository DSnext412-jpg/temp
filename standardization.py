import pandas as pd
from sklearn.preprocessing import StandardScaler

df=pd.DataFrame({"Age":[22,25,28,32,35],
                 "Salary":[25000,30000,40000,50000,60000],
                 "Experience":[1,3,5,8,10],
                 "Working_Hours":[35,40,42,45,50],
                 "Performance_Score":[60,65,72,80,90]})
print("Original Dataset:\n",df)
print("\nStandardized Data:\n",pd.DataFrame(StandardScaler().fit_transform(df),columns=df.columns))