class Node:
    def __init__(self, name):
        self.name=name
        self.children=[]

    def add(self, node):
        self.children.append(node)

def show(node,level=0):
    print("  " * level+node.name)
    for child in node.children:
        show(child,level+1)

root=Node("game")
a=Node("A")
b=Node("B")
c=Node("C")
d=Node("D")
root.add(a)
root.add(b)
a.add(c)
a.add(d)
show(root)