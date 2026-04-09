import sys
class Node:
    def __init__(self):
        self.data=data #instance variable
        self.next = None



class Linkedlist:
    def __init__(self):
        self.head =None
        self.tail =None


    def addNode(self,value):
        node = Node(value)
        if self.head is None:

            self.head= node
            self.head=node
        else:
            self.tail.next= node
            self.tail =node



if __name__=='__main__':
    object = Linkedlist()

    #menu driven option
    ''
    while True:
        print("1.add node linkedlist:")
        print("2.add node in beginning:")
        print("3.add node in between:")
        print("4.add node end:")
        print("5.display linked list")
        print("6.exit")

        ch=int(input("enter your choice:"))

        if ch == 1:
            Value = int(input("enter the value for node:"))
            object.addNode(Value)
            print("Node added successfully in single linkedlist")

        