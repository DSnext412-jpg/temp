import heapq
graph={
    "A":[("B",2),("C",4)],
    "B":[("A",2),("D",3),("E",5)],
    "C":[("A",4),("F",1)],
    "D":[("B",3),("F",2)],
    "E":[("B",5),("F",1)],
    "F":[("C",1),("D",2),("E",1)]
}

h={"A":6,"B":5,"C":3,"D":2,"E":1,"F":0}
queue=[(h["A"], "A")]
visited=set()

while queue:
    temp,node=heapq.heappop(queue)

    if node in visited:
        continue

    print(node,end=" ")
    visited.add(node)

    if node=="F":
        break

    for next_node,cost in graph[node]:
        if next_node not in visited:
            heapq.heappush(queue,(h[next_node],next_node))



"""
if you use this type of graph without wights its ok output will same 
becuase that no need weights only need of heuristic values

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "F"],
    "E": ["B", "F"],
    "F": ["C", "D", "E"]
}
"""