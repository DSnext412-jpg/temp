#slip 20 Q1 
def f(x):
    return -x**2+4*x
x=0
while True:
    if f(x+1)>f(x):
        x+=1
    elif f(x-1)>f(x):
        x-=1
    else:
        break
print("Maximum value:",f(x))
print("At x =",x)