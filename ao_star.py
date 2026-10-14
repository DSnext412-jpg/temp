graph={
    "A":[["B"],["C"]],
    "B":[["D"],["E"]],
    "C":[["F"],["G"]],
    "D":[["H"],["I"]],
    "E":[["J"]]
}
cost={
    ("A","B"):2,
    ("A","C"):3,
    ("B","D"):1,
    ("B","E"):4,
    ("C","F"):2,
    ("C","G"):5,
    ("D","H"):2,
    ("D","I"):3,
    ("E","J"):1
}

def ao_star(node):
    if node not in graph:
        return 0
    best=float("inf")
    for choice in graph[node]:
        total=0
        for child in choice:
            total+=cost[(node,child)]+ao_star(child)

        best=min(best,total)
    return best
print("Minimum Cost:",ao_star("A"))