# python desont support method overloading  

# class Arithamatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# obj=Arithamatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# class Arithamatic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("enter atleast two arguments")

# obj=Arithamatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)


# class  Arithematic:
#     def __init__(self):
#         print("there is no argument")

#     def __init__(self,a):
#         print("passing one argument")
    
#     def __init__(self,a,b):
#         print("passing  two arguments")

# # obj=Arithematic()
# # obj=Arithematic(10)
# obj=Arithematic(2,2)

# class Rbi:
#     def home_loan(self):
#         print("Home loan:7.5%")
#     def car_loan(self):
#         print("Car laon : 8%")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("Home Loan:6.5%")
#         super().home_loan()  #using super method you can access parent class method in child class 
# obj=Sbi()
# obj.home_loan()
# obj.car_loan()

#constructor overriding

class Father:
    def __init__(self):
        print("Father:i am already at the breakfast table ")

class Child(Father):
    def __init__(self):
        print("Child: i will be lte for breakfast")
        super().__init__()
        

obj=Child()



