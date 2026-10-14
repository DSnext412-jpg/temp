students=["Amit", "Riya", "John"]
def student(x):
    return x in students
def studies(x):
    return x in ["Amit", "Riya"]

for x in students:
    print(x, student(x), studies(x))
print("All students:", all(student(x) for x in students))
print("Some student studies:", any(studies(x) for x in students))

# read this it might can ask by external
# all() is a Python function that checks whether every condition inside it is True