import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("sales.csv")
print(df)
plt.boxplot(df["Sales"].dropna(),patch_artist=True,
            boxprops=dict(facecolor="skyblue"),
            medianprops=dict(color="red",linewidth=2),
            flierprops=dict(marker="o",markersize=8))
            
plt.title("Daily Sales Distribution and Outliers")
plt.ylabel("Sales Amount")
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.show()