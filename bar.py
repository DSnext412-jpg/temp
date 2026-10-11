import matplotlib.pyplot as plt
courses=["BCA","BBA","B.Com","B.Sc","BA"]
students=[60,45,75,50,35]
colors=['red','teal','skyblue','orange','green']

plt.bar(courses, students, color=colors)
plt.title("Number of Students Enrolled in Different Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")

plt.grid(axis="y",linestyle="--",alpha=0.5)
plt.show()