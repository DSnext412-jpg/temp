tree={
    "A":["B","C"],
    "B":[3,5],
    "C":[2,9]
}
def minimax(node,maximizing):
    if isinstance(node, int):
        return node
    values=[]
    for child in tree[node]:
        values.append(minimax(child,not maximizing))
    if maximizing:
        return max(values)
    else:
        return min(values)

print("Minimax Value:",minimax("A",True))