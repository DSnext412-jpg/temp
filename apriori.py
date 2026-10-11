import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data=[
 ["Video Lecture","Quiz"],
 ["Video Lecture","Assignment"],
 ["Quiz","Discussion Forum"],
 ["Video Lecture","Quiz","Assignment"],
 ["Assignment","Discussion Forum"],
 ["Video Lecture","Certificate"],
 ["Quiz","Certificate"],
 ["Video Lecture","Quiz"],
 ["Assignment","Certificate"],
 ["Video Lecture","Quiz","Certificate"]
]

te=TransactionEncoder()
df=pd.DataFrame(te.fit_transform(data), columns=te.columns_)

for s in [0.2, 0.3]:
    print(f"\nSupport {s}")
    freq=apriori(df, min_support=s, use_colnames=True)
    print(freq)
    print(association_rules(freq, metric="confidence", min_threshold=0.5)[["antecedents","consequents","confidence","lift"]])