class Node:
    def __init__(self, v = None):
        self.left: Node | None = None 
        self.right: Node | None = None 
        self.data = v

root = Node(5)
root.left = Node(4)
root.right = Node(9)
