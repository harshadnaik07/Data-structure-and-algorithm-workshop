
# #factorial solution
# def factorial(num):
#     if num <=1:
#         return 1
#     return num *factorial(num-1)

# print(factorial(4))


#palindrome

# def isPalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome('tacocat'))
# print(isPalindrome('awosome'))


# def power(base,exponent):
#     if exponent==0:
#         return 1
#     return base*power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))


# def capitalizeFirst(arr):

#     result=[]
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))



#productofArray solution

# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))

#fib solution

def fib(num):
    if(num<2):
        return num
    return fib(num-1)+fib(num-2)

print(fib(4))
print(fib(10))







