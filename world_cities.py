import pandas as pd, plotly.express as px
import matplotlib.pyplot as plt
import squarify

df=pd.read_csv("worldcities.csv")
print("world cities dataset:\n",df.head())
print("\nmissing values:\n",df.isnull().sum())

df=df.dropna(subset=["city","country","latitude","longitude","population"])
px.scatter_geo(df,lat="latitude",lon="longitude",size="population",color="country",
hover_name="city", hover_data=["population"],
title="world cities population visualization",projection="natural earth").show()

top=df.nlargest(20,"population")
plt.figure(figsize=(12,7))
squarify.plot(sizes=top["population"],label=top["city"],alpha=0.8)
plt.title("Population Distribution of Top 20 World Cities")
plt.axis("off")
plt.show()