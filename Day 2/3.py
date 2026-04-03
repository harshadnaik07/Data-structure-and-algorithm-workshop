# name=[4,2,5,6,8,2]
# for  i in name :
#     print(i)


# A=[4,0,2,5,0,1]

# for i in A :
#     if i==0:
#         A.remove(i)
#         A.append(i)
# print(A)


# A=[1,2,2,3,4,4,5]
# B=[]
# for i in A:
#     if i not in B:
#         B.append(i)

        
# print(B)



# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)


n=  int(input("enter size of array:"))
arr=[]
for i in range(n):
    val= int(input("enter the value of array:"))
    arr.append(val)
sum=0#12
print(arr)

for i in range (n):
    if i+1 in range(n):
        sum+= abs(arr[i]-arr[i+1])
print(sum)
 