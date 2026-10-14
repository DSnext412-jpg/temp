import heapq
graph={
    "A":{"B":1,"C":4},
    "B":{"D":2},
    "C":{"D":1},
    "D":{}
}
h={
    "A":3,
    "B":2,
    "C":1,
    "D":0
}

def astar(start, goal):
    queue=[(h[start], 0, start, [start])]
    visited=set()
    while queue:
        f,cost,node,path=heapq.heappop(queue)

        if node==goal:
            print("Path:",path)
            print("Cost:",cost)
            return
        if node in visited:
            continue
        visited.add(node)

        for next_node,value in graph[node].items():
            new_cost=cost+value
            heapq.heappush(
                queue,
                (new_cost+h[next_node],new_cost,
                 next_node,path+[next_node])
            )
astar("A", "D")