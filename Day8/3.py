# import re
# count =0
# pattern = re.compile("function")
# # print(pattern)
# matcher = pattern.finditer("A function in python is a block of code that performs a specific task. A function is a block of code that performs a specific task.")
# # print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())

# print("the number of occurence:",count)



# Q.2) WAP to perform finditer() program
# import re
# count=0
# matcher=re.finditer("hi","hihihihi")
# # print(matcher)
# for i in matcher:
#     count +=1
#     print(i.start(),"....",i.end(),"...",i.group())
# print("the number of occurence:",count)

# import re
# obj =input("enter any character")
# objmatch=re.finditer(obj,"a7b @k9z")
# # print(objmatch)
# for match in objmatch:
#     print(match.start(),"....",match.end(),"...",match.group())
# --------------------------------------------------------------------------
# import re 
# a= input("enter string to perform match operation:")
# mtch= re.match(a,"python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at begining level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at begining level")

# ---------------------------------------------------------------------------
# match() function

# for performing match 


# fullmatch()
# import re 
# a= input("enter string to perform match operation:")
# mtch= re.fullmatch(a,"pythonisvery")
# print(mtch)
# if mtch!=None:
#     print("match found")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("full match not found")

# -------------------------------------------------------------------------------

# search()function

# if the match found anywhere in the string then it return object else it will return None

# import re 
# a= input("enter string to perform match operation:")
# mtch= re.search(a,"python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
    
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("there is no matching anywhere ")


# --------------------------------------------------------------------------------

# findall() function
# import re
# mtch = re.findall('[0-9]',"abch3hdh5bk7zq$&*")
# print(mtch)




 # sub() function:substitute
# this function perform substitution or replacement


# import re
# obj= re.sub('[a-zA-Z]','X','2345 ABCD Fabc deff')
# print(obj)


# --------------------------------------------------------------------------------

# subn() function

# it  is as similar as sub() function only one thing is different that it also return number of replacement . this return in tuple where first element is string and second one is umber of replacement 

# import re
# obj  = re.subn('[0-7]','@','ab3gd6nkl7')
# print(obj)
# print(("the string is =",obj[0]))
# print("the number of replacement is = ",obj[1])
# #1234$dhfj$123dfgh$sdfghjk


#wap to check the valid mobile number

# import re
# mo=input("enter mobile number")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj !=None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")

#valid gmail id or not?
# import re
# s=input("enter mail id:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("valid E-mail ID")
# else:
#     print("Invalid E-mail Id")


#write a program to check whether the given file exists or not 


import os,sys
fname=input("enter file name :")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,"r")
else:
    print("file does not exists:",fname)
    sys.exit(0)
print("the content of file i:")
data=f.read()
print(data)


