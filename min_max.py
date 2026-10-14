import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler, Normalizer

df=pd.DataFrame({"Temperature":[20,25,30,35,40],
                 "Humidity":[40,50,60,70,80],
                 "Wind-Speed":[10,15,20,25,30],
                 "Pressure":[1000,1010,1020,1030,1040],
                 "Rainfall":[50,100,150,200,250]}
        )
print("Original Dataset:\n",df)

print("\nMin-Max Scaled Data:\n",pd.DataFrame(MinMaxScaler().fit_transform(df),columns=df.columns))
print("\nStandardized Data:\n",pd.DataFrame(StandardScaler().fit_transform(df),columns=df.columns))
print("\nNormalized Data:\n",pd.DataFrame(Normalizer().fit_transform(df),columns=df.columns))
