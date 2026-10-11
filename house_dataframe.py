import pandas as pd
from sklearn.preprocessing import Normalizer

df=pd.DataFrame({
"City":["Mumbai","Pune","Delhi","Ahmedabad","Bengaluru"],
"House_Type":["1BHK","2BHK","3BHK","2BHK","1BHK"],
"House_Area":[550,900,1400,1000,600],
"Number_of_Rooms":[2,3,4,3,2],
"Monthly_Rent":[18000,25000,40000,22000,20000]
})

print("Original Dataset:")
print(df)

cols=["House_Area","Number_of_Rooms","Monthly_Rent"]
norm_df=pd.DataFrame(Normalizer().fit_transform(df[cols]), columns=cols)

print("\nNormalized Data:")
print(norm_df)