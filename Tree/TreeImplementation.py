#Structue for Node!
class Node:
    def __init__(self,data):
        self.data=data
        self.left = self.right = None

#Actual Class
class Tree:
    def __init__(self):
        self.root = None
#pre-order
    def preorder(self,root):
        if root is None:
            return 
        print(root.data, end="->")
        self.preorder(root.left)
        self.preorder(root.right)

#Inorder
    def Inorder(self,root):
        if root is None:
            return 
        self.Inorder(root.left)
        print(root.data, end="->")
        self.Inorder(root.right)

#post-order
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end="->")

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

#Printing the Preorder
    print("Pre-Order Traversal:")
    tree.preorder(tree.root)
    print()
    
#Printing the Inorder
    print("InOrder Traversal:")
    tree.Inorder(tree.root)
    print()

#Printing the Postorder
    print("PostOrder Traversal:")
    tree.postorder(tree.root)
    print()
