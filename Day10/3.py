class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertNode(self, nodeValue):
        if self.data is None:
            self.data = nodeValue
        elif nodeValue < self.data:
            if self.leftChild is None:
                self.leftChild = BSTNode(nodeValue)
            else:
                self.leftChild.insertNode(nodeValue)
        else:
            if self.rightChild is None:
                self.rightChild = BSTNode(nodeValue)
            else:
                self.rightChild.insertNode(nodeValue)

        return "The value has been successfully inserted"
    
    def preOrderTraversal(rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        BSTNode.preOrderTraversal(rootNode.leftChild)
        BSTNode.preOrderTraversal(rootNode.rightChild)

    def inOrderTraversal(rootNode):
        if not rootNode:
            return
        BSTNode.inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        BSTNode.inOrderTraversal(rootNode.rightChild)

    def postOrderTraversal(rootNode):
        if not rootNode:
            return
        BSTNode.postOrderTraversal(rootNode.leftChild)
        BSTNode.postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

    

newBST = BSTNode(None)
newBST.insertNode(70)
newBST.insertNode(50)
newBST.insertNode(90)
newBST.insertNode(30)
newBST.insertNode(60)
newBST.insertNode(80)
newBST.insertNode(100)
newBST.insertNode(20)
newBST.insertNode(40)


print("inOrederTraversal")
BSTNode.inOrderTraversal(newBST)
print()

print("preOrderTraversal")
BSTNode.preOrderTraversal(newBST)
print()

print("postOrderTraversal")
BSTNode.postOrderTraversal(newBST)