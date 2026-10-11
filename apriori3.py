import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions=[
 ["Library","Seminar"],
 ["Workshop","Project"],
 ["Library","Assignment"],
 ["seminar","workshop"],
 ["Assignment","Seminar"],
 ["Workshop","Assignment"],
 ["Project","Library"],
 ["Library","Seminar","Project"],
 ["Library","Seminar","Workshop"]
]

te=TransactionEncoder()
df=pd.DataFrame(te.fit(transactions).transform(transactions), columns=te.columns_)
print("\nOne-Hot Encoded Dataset:\n",df)

for s in [0.2,0.3]:
  print(f"\nSupport={s} \nFrequent Itemsets:");f=apriori(df,min_support=s,use_colnames=True);print(f)
  if len(f)>1:
    r=association_rules(f,metric="confidence",min_threshold=0.5)
    print("\nassociation rules:\n",r[["antecedents","consequents","support","confidence","lift"]] 
    if not r.empty else "no association rules found")
  else:
    print("\nNo association rules found.")