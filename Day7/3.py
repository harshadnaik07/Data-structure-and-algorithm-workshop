# time complexity -
# 0(1) represents constant time

# Big O Notation
# O(1)        -   Constant Time       -   Accessing a specific eleement in array
# O(n)        -   Linear Time         -   Loop through array elements
# O(log n)    -   Logarithmic Time    -   Find an element in sorted array
# O(n^2)      -   Quadratic Time      -   Looking at every index in the array twice
# O(2^n)      -   Exponential Time    -   Double recursion in Fibonacci
# O(n log n)  -   Log-Linear Time     -   Merge Sort

# O(1) - Constant Time
# array = [1,2,3,4,5]
# array[0] //It takes constant time to access first element

# O(n) - Linear Time
# array = [1,2,3,4,5]
# for element in array:
#     print(element)) //Linear time since it is visiting every element of the array4


# O(LogN)-Logarithmic time
# array = [1,2,3,4,5]
# for index in range(0, len(array), 3):
#     print(array[index])
#     //Logarithmic time since it is visiting only some elements

# O(N^2)-Quadratic time 
# array = [1,2,3,4,5]

# for x in array:
#     for y in array:
#         print(x,y)

# O(2^N)-Exponential time
# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1)+fibonacci(n-1)

                                   # Time Complexity             Space Complexity
# Create Stack                             O(1)                        O(1)
# Push                                 O(1)/O(n^2)                     O(1)
# Pop                                      O(1)                        O(1)
# Peek                                     O(1)                        O(1)
# isEmpty                                  O(1)                        O(1)
# Delete Entire Stack                      O(1)                        O(1)



# There are 2 ways to implement stack : 1) Array 2)Linked list

# stack using list
#      - Easy to implement
#      - Speed problem when it grows

# stack using linked list
#      - Faster performance 
#      - Implementation is not easy



#                             Time Complexity     Space Complexity
# Create Queue                      O(1)                 O(1)
# Enqueue                           O(n)                 O(1)
# Dequeue                           O(n)                 O(1)
# Peek                              O(1)                 O(1)
# isEmpty                           O(1)                 O(1)
# Delete Entire Queue               O(1)                 O(1)


# queue using list
#     -easy to implement
#       -speed problem when it grow

# queue using linked list
#       - fast performance
        # - implementation is not easy

# def FindBiggestNumber(array):
#     firstvalue=array[0]
#     for i in range(1,len(array)):
#         if array[i]>firstvalue:
#             firstvalue=array[i]
#     return firstvalue
# array=[1,2,3,4,5]
# print(FindBiggestNumber(array))


# def findBiggestNumber(array):------------------->O(1)
#     firstvalue=array[0]------------------------->O(1)
#     for i in range(1,len(array)):--------------->O(n)----->
#         if array[i]>firstvalue:----------------->O(1)----->O(n) #overall complexity is the O(n)
#             firstvalue=array[i]----------------->O(1)----->
#     print(firstvalue)--------------------------->O(1)
    
# array=[2,4,5,6,7,1,9,3,4,5,6]
# findBiggestNumber(array)


# A="gasgg54@#vscsd$#"
# count=0

# for i in A:
#     if not i.isalnum():
#         count+=1

# print(count)






# A=[79,77,54,81,48,34,25,16]

import math

A=[79,77,54,81,48,34,25,16]
Count=0 
for i in A:
    if math.sqrt(i)==math.sqrt(i)//1:
        Count+=1
print("the total square plots are ",Count)




