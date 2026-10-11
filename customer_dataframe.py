import pandas as pd
from sklearn.preprocessing import LabelEncoder
data={
    "Customer_ID":[101,102,103,104,105],
    "Gender":["Male","Female","Female","Male","Female"],
    "City":["Pune","Mumbai","Nashik","Pune","Mumbai"],
    "Membership_Type":["Gold","Silver","Gold","Platinum","Silver"]
}
df=pd.DataFrame(data)
print("Before Encoding:")
print(df)

labelencoding=LabelEncoder()
for column in ["Gender","City","Membership_Type"]:
    df[column]=labelencoding.fit_transform(df[column])

print("\nAfter Encoding:")
print(df)