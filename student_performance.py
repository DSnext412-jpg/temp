import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame({
 "Study Hours":[2,3,4,5,6,7,8,9],
 "Attendance":[65,70,75,80,82,88,92,95],
 "Assignment Score":[55,60,65,72,75,82,88,92],
 "Exam Score":[50,58,63,70,74,80,87,94]
})

print(df)
print("\nCorrelation Matrix:\n",df.corr())

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm",fmt=".2f")
plt.title("correlation Heat Map ;")
plt.show()