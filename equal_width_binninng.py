import pandas as pd 
age_records=pd.DataFrame({ 
    "Person_ID":[101,102,103,104,105,106,107,108,109,110], 
    "Age":[18,22,27,31,36,42,48,55,63,72] 
}) 
age_records["Age_Bin"] = pd.cut( 
    age_records["Age"], 
    bins=4, 
    labels=["young","adult", "middle aged","senior"] 
) 
print("original and discretized data: ") 
print(age_records) 