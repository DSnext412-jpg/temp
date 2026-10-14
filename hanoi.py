def hanoi(n,source,target,spare):
    if n==1:
        print(source,"->",target)
        return
    hanoi(n-1,source,spare,target)
    print(source,"->",target)
    hanoi(n-1,spare,target,source)

hanoi(3,"A","C","B")