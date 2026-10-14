graph={
    "A":["B","C","E"],
    "B":["A","D"],
    "C":["A","F"],
    "D":["B","E"],
    "E":["D","A","F"],
    "F":["C","E"]
}
visited = set()
def dfs(node):
    if node in visited:
        return
    print(node, end=" ")
    visited.add(node)
    for child in graph[node]:
        dfs(child)
dfs("A")