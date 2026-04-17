class Node:
    # creating a separate node in the tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # INSERT NODE
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, rootNode, value):
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left, value)
        else:
            if rootNode.right is None:
                rootNode.right = Node(value)
            else:
                self.insertNode(rootNode.right, value)

    # SEARCH NODE
    def search(self, value):
        return self.searchNode(self.root, value)

    def searchNode(self, rootNode, value):
        if rootNode is None:
            return False
        if rootNode.value == value:
            return True
        elif value < rootNode.value:
            return self.searchNode(rootNode.left, value)
        else:
            return self.searchNode(rootNode.right, value)

    # PRINT TREE (LEVEL ORDER)
    def printTree(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = []
        queue.append(self.root)

        print("Tree elements are:")
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    # DELETE TREE
    def deleteTree(self):
        self.root = None


# ----------- MENU (SWITCH) -----------
btObj = BinaryTree()

while True:
    print("\n1.Insert")
    print("2.Search")
    print("3.Print Tree")
    print("4.Delete Tree")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            val = int(input("Enter value to insert: "))
            btObj.insert(val)

        case 2:
            val = int(input("Enter value to search: "))
            if btObj.search(val):
                print("Value Found")
            else:
                print("Value Not Found")

        case 3:
            btObj.printTree()

        case 4:
            btObj.deleteTree()
            print("Tree Deleted")

        case 5:
            print("Program Ended")
            break

        case _:
            print("Invalid choice")