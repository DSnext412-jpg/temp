import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
data=[["Basmati Rice","Toor Dal","Turmeric Powder","Cooking Oil"],
["Atta","Sugar","Tea","Milk"],
["Rice","Moong Dal","Salt","Cooking Oil"],
["Wheat Flour","Chickpeas","Turmeric Powder","Cumin Seeds"],
["Poha","Peanuts","Onions","Cooking Oil"],
["Basmati Rice","Paneer","Garam Masala","Tomatoes"],
["Atta","Potatoes","Onions","Cooking Oil"]]

te=TransactionEncoder()
df=pd.DataFrame(te.fit(data).transform(data),columns=te.columns_)
print("\none hot encoded dataset:\n",df)
print("\nmissing values after encoding:\n",df.isnull().sum())

df=df.fillna(False)
for s in [0.3,0.4]:
    print("\nMinimum Support =",s)
    f=apriori(df,min_support=s,use_colnames=True)
    print(f)
    if len(f)>1:
        print(association_rules(f,metric="confidence",min_threshold=0.5))[["antecedents","consequents","support","confidence","lift"]] 
