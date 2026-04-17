# A=6
# B=13
# C=[10,15,23,14,2,15]

# count=0

# for i in range(len(C)):
#     for j in range(len(C)):
#         if C[j]-C[i]==B:
#             count+=1

# print(count)






A=int(input())
B=[]

for i in range(2,A+1):
    for j in range(2,i):
        if i%2==0:
            break
    else:
        print(i,end=" ")
    