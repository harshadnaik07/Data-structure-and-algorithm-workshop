# class Base:
#     def __init__(self):
#         print("parent class constructor  called")
#         self.a="prashant"   #public data member
#         self.__c="Ashish"
# #creating a private class/child class
# class Derived(Base):
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         #print("calling private member of base class:")
#         # print(self.a)
#         # print(self.__c)



# # obj1=Derived()
# # print(obj1.a)
# # print(obj1.__c)

# obj2= Base()
# print(obj2.a)#Accessibel 
# print(obj2.__c)#not Accessibel




class Rbi:

    def publicPolicy(self):
        print("check the public Policy of RBI")

    def __privatepolicy(self):
        print("there is some private policy which is not accessible for public")




class Sbi(Rbi):
    def __ini__(self): #first sbi class const called
        Rbi.__init__(self) #secound parent class constr called

    def callingPublicMethod(self): #child class public method
        print("\nIside child class")
        self.publicPolicy() #Calling parent class public method 

    def  classprivateMethod(self):  #child class public method
        self.__privatepolicy()  #calling parent class private method

# obj1 = Sbi()
# obj1.callingPublicMethod()      
# obj1.classprivateMethod()
# obj1.publicPolicy()
# obj1.__privatepolicy()

# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatepolicy()
# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatepolicy()
# obj2=Rbi()
# obj2.publicPolicy()
# obj2._Rbi_privatePolicy()
