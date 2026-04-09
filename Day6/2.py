# from abc import ABC,abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def tranning(self):
#         pass
#     @abstractmethod
#     def placement(self):
#         pass

# class Ashish(Help4code):
#     def tranning(self):
#         print('c','c++','java')
#     def placement(self):
#         print("java placement")

# class Ankush(Help4code):
#     def tranning(self):
#         print('python','django')
#     def placement(self):
#         print("python placement")
    
# class prashant(Help4code):
#     def tranning(self):
#         print('machine learning')
#     def placement(self):
#         print("Data science placement")

# obj1=Ashish()
# obj1.tranning()
# obj1.placement()

# obj2=Ankush()
# obj2.tranning()
# obj2.placement()

# obj3=prashant()
# obj3.tranning()
# obj3.placement()








from abc import ABC,abstractmethod
class Irctc(ABC):

    @abstractmethod
    def bookticket(self):
        pass

class Makemytrip(Irctc):

    def bookticket(self):
        print("=======================================")
        print("welcome to make my trip")
        source=input("enter a source station name:")
        destination=input("enter destination name :")
        date = input("enter date")

        print("=========================================")

class GoIbibo(Irctc):
    def bookticket(self):
        
        print("===========================================")
        print("welcome to GOibibo")
        source=input("enter a source station name:")
        destination=input("enter destination name :")
        date = input("enter date")

        print("=========================================")

obj1=Makemytrip()
obj1.bookticket()

obj2=GoIbibo()
obj2.bookticket()