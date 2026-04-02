# username= input(" enter username:")
# password = input("enter password:")

# if username==password:
#     print("login successful")
# else:
#     print("invalid credential")


#wap  to accept phy,chem and math subject marks calculate total and percentage and if percentage is grater than equal to 60 and gender is equal to male so he is eligible for placement else eligible for data entry job

# phy = int(input("enter marks for phy:"))
# chem = int(input("enter marks for chem:"))
# math = int(input("enter marks for math :"))
# gender=input("enter your gender:")
# total = phy+chem+math

# percentage = total/3

# print("total:",total)
# print("percentage:",percentage)

# if percentage >= 60 and gender == "male" :
#     print("you are eligible for placement ")
# else:
#     print("eligivel for data entary ")


#Q.nested if else: wap to accept value of A,B,C and find max value 

# a= int(input("enter a number"))

# b= int(input("enter a number"))
# c= int(input("enter a number"))

# if a>b :
#     if a>c:
#         print("a is greater:",a)
#     else:
#         print("c is greater :",c)

# else:
#     if b>a:
#         if b>c:
#             print("b is greater:",b)
#         else:
#             print("c is grater:", c)

#Q.
# days = input("enter the day :")

# if days == "saturday" or days == "Saturday" or days == "sunday" or days == "Sunday":
#     print("off day ")
# else:
#     print("working day ")


ch =ord(input("enter any character "))

if ch>=65 and ch<=91:
    print("your entered character is in uppercase")
elif ch>=97 and ch<=122:
    print("you enter character in lower case")
elif ch>=48 and ch<=57:
    print("you enter character in digit ")
else:
    print("you enterd character is in special symbols")
