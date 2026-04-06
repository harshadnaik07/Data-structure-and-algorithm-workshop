import sys

class CRUD:
    def __init__(self):
        print("student management system")

        self.studentID=[]
        self.studentName=[]
        self.studentRollno=[]
        self.studentCity=[]

    def addStudent(self):
        self.studentID.append(int(input("enter student id :")))
        self.studentName.append(input("enter student name :"))
        self.studentRollno.append(int(input("enter roll no :")))
        self.studentCity.append(input("enter your city"))

    def showStudent(self):
        print("studenID:",self.studentID)
        print("student name:",self.studentName)
        print("student rollno:",self.studentRollno)
        print("student city :",self.studentCity)

        
obj=CRUD()
obj.addStudent()
obj.showStudent()


while True:
    print("enter your choice ")
    print("1.add student:")
    print("2.show student:")
    print("3.exit:")

    choice= int(input("enter your choice:"))

    if choice==1:
        obj.addstudent()
    elif choice == 2:
        obj.showStudent()
    elif choice==3:
        sys.exit()

    

