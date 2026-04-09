class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head =None

linkedlist = LinkedList()


linkedlist.head= Node(5)
second          =Node(10)
third           =Node(15)
fourth          =Node(20)

print(linkedlist.head.data)
print(second.data)
print(third.data)
print(fourth.data)


print(linkedlist.head.next)
print(second.next)
print(third.next)
print(fourth.next)

linkedlist.head.next=second
second.next=third
third.next=fourth





#linking part

linkedlist.head.next = second
second.next=third


#display linkedlist

while linkedlist.head != None:
    print("|",linkedlist.head.data,"|",linkedlist.head.next,"->",end=" ")
    linkedlist.head=linkedlist.head.next




