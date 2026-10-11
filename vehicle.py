import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({"Fuel Effi":[18,22,20,25,80],
                 "engine power":[120,150,135,180,500],
                 "vehicle weight":[1200,1400,1300,1500,1600],
                 "engine size":[1.5,1.8,1.6,2.0,12.5],
                 "accelaration":[10.5,9.2,10.0,8.5,6.0]})
print("Vehicle DataFrame:\n",df)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.boxplot(df["Fuel Effi"])
plt.title("Box Plot - Fuel Efficiency")

plt.subplot(1,2,2)
plt.boxplot(df["engine power"])
plt.title("Box Plot - Engine Power")

plt.tight_layout()
plt.show()

def outliers(col):
    Q1,Q3=df[col].quantile(0.25),df[col].quantile(0.75)
    IQR=Q3-Q1
    L=Q1-1.5*IQR
    U=Q3+1.5*IQR
    return Q1,Q3,L,U,df[(df[col]<L)|(df[col]>U)][col]

for c in ["Fuel Effi","engine power"]:
    q1,q3,l,u,o=outliers(c)
    print(f"\n{c}:\nQ1={q1}\nQ3={q3}\nlower limit={l}\nupper limit={u}\noutliers={list(o)}")