colors = ["Red", "Green", "Blue","Yellow"]
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["C", "B"]
}
color={}
def solve(node):
    if node==len(graph):
        return True
    name=list(graph)[node]
    for c in colors:
        if all(color.get(n) != c for n in graph[name]):
            color[name] = c
            if solve(node + 1):
                return True
            del color[name]
    return False

solve(0)
print(color)




# read this it might can ask by external
# all() is a Python function that checks whether every condition inside it is True.