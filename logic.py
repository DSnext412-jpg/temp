print("P\tQ\tP AND Q\tP OR Q\tNOT P") 

for P in [0,1]: 
    for Q in [0,1]: 
        print(f"{P}\t{Q}\t{P and Q}\t{P or Q}\t{int(not P)}") 

print("\n(P AND Q) OR NOT R = ",(P and Q) or (not P))


"""
                  ----OR----
P=True
Q=False
print("(P AND Q) =",P and Q)
print("(P OR Q ) = ",P or Q)
print("(NOT P) = ",not P)


"""

print("T\tF\tT AND F\tT OR F\tNOT T\t(T AND F) OR (NOT T)")
print("----------------------------------------------------")

T,F=True,False

for T in [0, 1]:
    for F in [0, 1]:
        expr=int((P and Q) or (not P))
        print(f"{T}\t{F}\t{T and F}\t{T or F}\t{(not T)}\t{expr}\n")


print("T AND F =",T and F)
print("T OR F  =",T or F)
print("NOT T   =",not T)
print("(T AND F) OR (NOT T) =",(T and F)or(not T))