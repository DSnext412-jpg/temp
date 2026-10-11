import pandas as pd, seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({"Temperature":[20,22,26,30,34,32,29,28,29,27,24,21],
                 "Humidity":[60,58,55,52,60,78,88,90,85,75,68,63],
                 "Rainfall":[15,20,30,45,70,180,320,290,210,90,35,18],
                 "Wind Speed":[12,14,16,18,20,22,25,23,20,17,15,13]})
sns.heatmap(df.corr(),annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5)
plt.title("Correlation Heat Map of Weather Parameters"); 
plt.show()