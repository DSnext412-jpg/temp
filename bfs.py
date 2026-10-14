from collections import deque
graph={
    1:[2,3],
    2:[4,5],
    3:[6,7],
    4:[8,9],
    5:[10,11],
    6:[12,13],
    7:[14,15],
    8:[],9:[],10:[],11:[],
    12:[],13:[],14:[],15:[]
}
visited=set()
queue=deque(['1'])
while queue:
    node=queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(graph[node])



"""
other graphs :


    "A":["B", "C"],
    "B":["D"],
    "C":["E"],
    "D":["E"],
    "E":[]

"""