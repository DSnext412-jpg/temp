import matplotlib.pyplot as plt 
departments=["HR","Finance","IT","Sales","Marketing"] 
employees=[20, 30, 50, 40, 25] 
colors=["red","blue","green","orange","purple"] 
plt.bar(departments,employees,color=colors)
plt.title("number of students enrolled in different courses")
plt.xlabel("courses")
plt.ylabel("number of students")

plt.grid(axis="y",linestyle="--",alpha=0.5)
plt.show()