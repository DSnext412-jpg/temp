from collections import deque
states = [
    "Monkey on floor",
    "Monkey push box",
    "Monkey on box",
    "Monkey gets banana"
]
q=deque(["Monkey on floor"])
visited=set()

while q:
    state=q.popleft()
    if state in visited:
        continue
    print(state)
    visited.add(state)
    if state=="Monkey on floor":
        q.append("Monkey push box")
    elif state=="Monkey push box":
        q.append("Monkey on box")
    elif state=="Monkey on box":
        q.append("Monkey gets banana")