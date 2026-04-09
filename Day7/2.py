import sys
class Queue:
    def __init__(self,queueSize):
        self.queueList =[] # Queue created
        self.queueSize = queueSize
        
    def isFull(self):
        if len(self.queueList)== self.queueSize:
            return True
        else: 
            return False
        
    def Enqueue(self, value):
        if self.isFull():
            print("Queue is full")
            
        else:
            self.queueList.append(value)
            
        
        
    def displayQueue(self):
        print(self.queueList)
        
    def isEmpty(self):
        if self.queueList ==[]:
            return True
        else:
            return False
        
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty:")
        else:
           return self.queueList.pop()
       
    def deleteQueue(self): # delete the queue
        self.queueList = []
        return "Queue is deleted"
    
    def peek(self): #it return the first element of Queue
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queueList[0] # slicing of list
        
    
        
size = int(input("Enter the size of Queue : ")) 
print()
print("Queue has been created with size ",size)      
queueObj = Queue(size) # Queue object has created 
        

while True:
    1
    
    print("1.Enqueue element in Queue ")
    print("2.Display Queue element")
    print("3.Check Queue IsEmpty ")
    print("4.Pop Operation")
    print("5.Delect full Queue")
    print("6.Peek Operation")
    print("7.Exit from system")
    
    choice = int(input("Enter your choice : "))
    if choice == 1:
       val = int(input("Enter the value for stack : "))
       queueObj.Enqueue(val)
    elif choice ==2:
        queueObj.displayQueue()
        
    elif choice ==3:
        print(queueObj.isEmpty())
        
    elif choice == 4:
        print(queueObj.Dequeue())
        
    elif choice == 5:
        print(queueObj.deleteQueue())
        
    elif choice == 6:
        print(queueObj.peek())
        
    elif choice == 7:
        sys.exit()