# import QueueLinkedList as queue

# class BSTNode:

#     def __init__(self,data):
        


class Node:
    #create anode in the tree
    def __init__(self,value):

        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    

    def insert(self,value):
        #insert root node in if there is no root node
        if self.root is  None:
            self.root = Node(value)
        else:
            self.insertNode(self.root,value)

    
    def insertNode(self,rootNode,value):
        if value <rootNode.value:
            #inserting node in the left and right position
            if rootNode.left is None:
                rootNode.left=Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right=Node(value)
            else:
                self.insertNode(rootNode.left,value)


btobj=BinaryTree()
btobj.insert(50)
btobj.insert(50)
            
print(btobj)

