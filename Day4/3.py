# #exception

# # n1= int(input("enter the first value:"))
# # n2= int(input("enter the secound value:"))

# # try:
# #     print(n1/n2)
# # except:
# #     print("can't divide by zero ")

# # print("To be continue")





# # exception
# try:
#     n1= int(input("enter the first value:"))
#     n2= int(input("enter the secound value:"))

#     print(n1/n2)
# except ZeroDivisionError:
#     print("can't divide by zero ")

# except ValueError:
#     print("enter only integer value")

# print("To be continue")





# try:
#     n1=int(input("enter the value 1:"))
#     n2=int(input("enter the second value "))

#     print(n1/n2)
    
# except(ValueError,ZeroDivisionError) as message:
#     print(message)



# try:
#     n1=int(input("enter the value 1:"))
#     n2=int(input("enter the second value "))

#     print(n1/n2)
    
# except(ValueError,ZeroDivisionError) as message:
#     print("enter the correct number:",message)

# except:
#     print("this is a default part of except block")



# try:
#     n1=int(input("enter the value 1:"))
#     n2=int(input("enter the second value "))

#     print(n1/n2)
    
# except(ValueError,ZeroDivisionError) as message:
#     print("enter the correct number:",message)

# else:
#     print("everything is ok")



# try:
#     n1=int(input("enter the value 1:"))
#     n2=int(input("enter the second value "))

#     print(n1/n2)
    
# except(ValueError,ZeroDivisionError) as message:
#     print("enter the correct number:",message)

# finally:
#     print("i will always executed")



#nested try except block
try:
    n1=int(input("enter the value 1:"))
    n2=int(input("enter the second value "))

    try:
        print(n1/n2)
    except ZeroDivisionError as msg:
        print(msg)


except ValueError as msg:
    print(msg)



# try:
#     n1=int(input("enter the value 1:"))
#     n2=int(input("enter the second value "))

#     print(n1/n2)
    
# except(ValueError,ZeroDivisionError) as message:
#     print("enter the correct number:",message)

# else:
#     print("there is no error in try block")
# finally:
#     print("i will always executed")










  













