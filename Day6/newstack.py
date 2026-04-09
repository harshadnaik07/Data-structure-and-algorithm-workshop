import sys
class Stack:
    def __init__(self, stackSize):
        self.stacklist = []
        self.stackSize = stackSize
        
    def isFull(self):
        if len(self.stacklist) == self.stackSize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            print("stack is full")
        else:
            self.stacklist.append(value)

    def display(self):
        print("---------------------------")
        print(self.stacklist)
        print("---------------------------")

    def isEmpty(self):
        if self.stacklist == []:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stacklist.pop()
        
    def delete(self):
        self.stacklist = None
        print("stack is deleted")

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stacklist[-1]
        

size = int(input("Enter the size of the stack: "))
stackobj =  Stack(size)

while True:
    
    print("1.push element")
    print("2.display stack element")
    print("3. check isEmpty")
    print("4.pop element")
    print("5.delete stack")
    print("6.peek operation")
    print("7.Exit")



    choice = int(input("enter your choice:"))
    if choice == 1 :
        val= int(input("enter the value for stack:"))
        stackobj.push(val)

    elif choice == 2:
        stackobj.display()
    
    elif choice == 3:
       print(stackobj.isEmpty())
    
    elif choice == 4:
        print(stackobj.pop())

    elif choice == 5:
        stackobj.delete()

    elif choice == 6:
        stackobj.peek()
    
    elif choice == 7:
        sys.exit()
    else:
            print("Invalid choice, please try again.")