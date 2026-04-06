# class Student:
#     roll_no=101

#     def studentData(self):
#         print("student information")


# obj=Student()
# print(obj.roll_no)
# # obj.studentData()

# class Demo :
#     def __init__(self):
#         print("i am constructor")
    
#     def msg(self):
#         print("hello class")
# obj1=Demo()
# print(obj1)
# obj2=Demo()
# obj1.msg()
# obj2.msg()


# class Hod:
#     def __init__(self):
#         self.name='harshad naik'
#         self.age=19
#         self.empid=1001
#     def info(self):
#         print("my name is :",self.name)
#         print("my age is :",self.age)
#         print("my emp id :",self.empid)
# obj=Hod()
# obj.info()



# class Hod:
#     def __init__(self,name,age,roll_no):
#         self.name=name
#         self.age=age
#         self.roll_no=roll_no
#     def info(self):
#         print("my name is :",self.name)
#         print("my age is :",self.age)
#         print("my emp id :",self.roll_no)
# obj=Hod("harshad",19,36)
# obj.info()

# class New():
#     def __init__(self):
#         self.a=10

# obj1=New()
# obj2=New()
# obj3=New()


# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# print()
# obj1.a=20



# print(obj1.a)
# print(obj2.a)
# print(obj3.a)




# class Student:
#     def __init__(self):
#         self.s_name="harshad"
#         self.s_rollno=36

#     def getdata(self):
#         self.s_mb=123456789


# obj=Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch='cs'
# print(obj.__dict__)



# class New:
#     a=10
    

#     def __init__(self):
#         self.name="harshad"

# obj1=New()
# obj2=New()
# obj3=New()


# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# New.a=50
# print(obj1.a)
# print(obj2.a)



# print(obj3.a)


# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name=name   #instace variable 
#         self.rollno=rollno
#         self.mob=mob

#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)

# stud = Student("harshad",36,1023456098)
# stud.display()

class Student:
    @staticmethod
    def get_personal_details(firstname,lastname):
        print("your personal details=",firstname,lastname)
        
    @staticmethod
    def contact_details(mobil_no,rollno):
        print("your conntact details=",mobil_no,rollno)

Student.get_personal_details("harshad","naik")
Student.contact_details(23145562312,1001)





