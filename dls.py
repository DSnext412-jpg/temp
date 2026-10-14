graph={
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":[]
}
def dls(node, goal, depth):
    print(node, end=" ")
    if node==goal:
        return True
    if depth==0:
        return False
    for child in graph[node]:
        if dls(child, goal,depth-1):
            return True
    return False

dls("A", "F", 2)