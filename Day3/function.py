# # # # # # def msg():
# # # # # #     print("hello")

# # # # # # msg()
# # # # # # msg()


# # # # # def arithematic():
# # # # #     a= int(input("enter the value of A:"))
# # # # #     b= int(input("enter the value of B:"))
# # # # #     add= a+b
# # # # #     sub=a-b
# # # # #     mul=a*b
# # # # #     div=a/b

# # # # #     return add,sub,mul,div

# # # # # # print(arithematic())

# # # # # result=arithematic()
# # # # # print("arithematic=",result)
  


# # # # #how many types of argument we can pass in function
# # # # # 1.positional argument
# # # # # 2.keyword argument
# # # # # 3.defaul argument
# # # # # 4.variable number of argument/variable length argument


# # # # def login(username,password):
# # # #     if username==password:
# # # #         print("login successfully")
# # # #     else:
# # # #         print("invalid creadential")
# # # # username=input("enter user name:")
# # # # password=input("enter password :")

# # # # login(username,password)






# # # #keyword argument
# # # def login(username,password):
# # #     if username==password:
# # #         print("login successfully")
# # #     else:
# # #         print("invalid creadential")


# # # login(username="admin",password="admin")




# # #default argument

# # def cityName(city="goa"):
# #     print(city)

# # cityName("delhi")
# # cityName("mumbai")
# # cityName("nagpur")
# # cityName()


# #variable length argument/variable number of argument


# def nameofcitys(*city):
#     print("citynames=",city)

# nameofcitys("goa","nashik","mumbai","pune")
