# def linearSearch(array,target):    #array=[1,2,3,4,5,6,7,8,9]
#     for i in range(len(array)): # ===================>o(n)
#         if array[i]==target:        # ===================>o(1)
#             return i
#     return -1
    


# array=[1,2,3,4,5,6,7,8,9]
# target=5
# result=linearSearch(array,target)
# if result == -1:
#     print("not found")
# else:
#     print("element found at index no=",result)


def binarysearch(array,target):
    start=0
    end=len(array)-1
    while start <=end:
        mid=start+end
        if array[mid]==target:
            return mid 
        elif array[mid]<target:
            start = mid+1
        else:
            end=mid-1
    return -1


sortedArray=[1,2,3,4,5,6,7,8,9]
target =5
result= binarysearch(sortedArray,target)    
if  result==-1:
    print("element not found")
else:
    print("element found at index",result)
