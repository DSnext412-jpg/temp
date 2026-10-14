def f(x):
    return-(x-3)**2+9
x=0

while True:
    current=f(x)
    if f(x+1)>current:
        x+=1
    elif f(x-1)>current:
        x-=1
    else:
        break
print("Maximum value:",f(x))
print("At x =",x)