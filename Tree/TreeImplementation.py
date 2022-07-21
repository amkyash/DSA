#Structue for Node!
class Node:
    def __init__(self,data):
        self.data=data
        self.left = self.right = None

#Actual Class
class Tree:
    def __init__(self):
        self.root = None

#Inserting Data in the Tree
if __name__ == "__main__":
    tree=Tree()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    print(tree.root)
    
    