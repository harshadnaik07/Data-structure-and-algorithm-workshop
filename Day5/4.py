#inheritance

#extending a property from one class to another class is called inheritance
#base class: parent class
#derived class : child class 

# class Collage:
#     def collage_name(self):
#         print("modern collage")

# class Student(Collage):
#         def student_info(self):
#             print("name:harshad")
#             print("branch: computer science")

# obj=Student()
# obj.collage_name()
# obj.student_info()


# class Collage :
#     def collage_name(self):
#         print("modern collage")

# class Student(Collage):
#     def student_info(self):
#         print("name:  harshad naik")
#         print("branch: computer science")

# class Exam(Student):
#     def subject(self):
#         print("subject1:: design engineering")
#         print("subject2:math")
#         print("subject3:python")

# obj=Exam()
# obj.collage_name()
# obj.student_info()
# obj.subject()


# class SubMarks:
#     math = int(input("enter paper marks for math: "))
#     DE= int(input("enter marks for DE:"))
#     c=int(input("enter paper marks for c language:"))
#     english=int(input("enter paper marks for english:"))

# class PractMarks:
#     cpract= int(input("enter practivcal marks of language:"))

# class Result(SubMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj=Result()
# obj.total()


class Principal:
    def role(self):
        print('i am managing all activity of collage')
class Dean:
    def role(self):
        print("dean= i am decision taking person")

class Hod:
    def role(self):
        print("hod = i have responsibility of teacher and student")
class Faculty:
    def role(self):
        print("faculty= i have to complete syllabus successfully")

def func(obj):
    obj.role()
campus=[Principal(),Dean(),Hod(),Faculty()]
for obj in campus:
    func(obj)

#







