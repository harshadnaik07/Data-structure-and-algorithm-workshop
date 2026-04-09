#Q1
# A="aaabbbccccc"
# b=" "

# for i in A:
#     if i not in b:
        
#          b+=i
#          b+=str(A.count(i))

    
    
# print(b)


#Q2

# A="Hello world "
# s= A.split()

# B=""

# for i in s:
#     B+=i[::-1]+" "
    
    
# print(A)
# print(B)


A= [10,98,3,33,12,22,21,11]
B=[]
C=[]

for  i in A:
    if (i%2==0): 
        B.append(i)
    else:
        C.append(i)

        
        

print(B+C)









