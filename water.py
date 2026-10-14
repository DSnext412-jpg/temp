from collections import deque
def bfs():
    q=deque([(0,0)])
    visited=set()
    while q:
        a,b=q.popleft()
        if (a,b) in visited:
            continue
        visited.add((a,b))
        print(a,b)
        if a==2 or b==2:
            break

        states = [
            (4,b),(a,3),
            (0,b),(a,0),
            (a-min(a,3-b),b+min(a,3-b)),
            (a+min(b,4-a),b-min(b,4-a))
        ]
        for s in states:
            if s not in visited:
                q.append(s)
bfs()