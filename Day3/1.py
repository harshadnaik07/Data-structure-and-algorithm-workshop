A = [-1,2,-3,4,5,-6]
B=[]
c=[]

for i in A:
    if i<0:
        B.append(i)

    else:
        c.append(i)

    # print(B)
    # print(c)

for i in range (len(B)):
    A[i*2]=B[i]
    A[i*2+1]=c[i]
print(A)


