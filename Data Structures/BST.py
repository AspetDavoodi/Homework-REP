class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:

    def __init__(self):
        self.root=None

    def __str__(self):
        if self.root is None:
            return "Root is None"
        else:
            return str(self.root.data)

    def addNode(self, node):
        if self.root is None:
            self.root = node
        elif self.root.data == node.data:
            print("Nodes cannot have the same value. Node has not been added")
        else:
            self.addToRoot(node,self.root)

    def addToRoot(self,node,root):
        if node.data<root.data:
            if root.left is None:
                root.left=node
            else:
                self.addToRoot(node,root.left)
        else:
            if root.right is None:
                root.right=node
            else:
                self.addToRoot(node,root.right)

    def printTree(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.printNode(self.root)

    def printNode(self,root):
        if root is not None:
            self.printNode(root.left)
            print(str(root.data))
            self.printNode(root.right)


def main():
    myBST = BST()
    print(myBST)

    myNode = Node(8)
    myBST.addNode(myNode)
    myNode = Node(8)
    myBST.addNode(myNode)
    myNode = Node(10)
    myBST.addNode(myNode)
    myNode = Node(9)
    myBST.addNode(myNode)
    myNode = Node(5)
    myBST.addNode(myNode)
    myNode = Node(3)
    myBST.addNode(myNode)
    myNode = Node(4)
    myBST.addNode(myNode)
    myBST.printTree()



main()