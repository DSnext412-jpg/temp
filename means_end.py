current=2
goal=5
while current!=goal:
    difference=goal-current
    if difference>0:
        print("Move:", current,"->", current+1)
        current += 1
    else:
        print("Move:",current,"->",current-1)
        current-=1
print("Goal reached:",current)