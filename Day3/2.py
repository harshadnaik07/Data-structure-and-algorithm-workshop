# # #Q
# # # a={(1,2):1,(2,3):2,(4,5):3}
# # # print(a[4,5])

# # #Q
# # a={'a':1,'b':2,'c':3}
# # # print(a['a','b'])

# # arr={}
# # arr[1]=1
# # arr['1']=2
# # arr[1]+=1

# # sum=0
# # for k in arr:
# #     sum+=arr[k]
# # print(sum)

# my_dict={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict)


# sum=0
# for i in my_dict:
#     sum+=my_dict[i]
# print(sum)





# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)
# print(my_dict)


# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))

# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# rec={"Name":"python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec))

# print(id(r))
# print(id(rec))

# rec={"Name":"python","Age":"20","addr":"NJ","countary":"USA"}
# id1=id(rec)
# print(id1)
# del rec
# rec={"Name":"python","Age":"20","addr":"NJ","countary":"USA"}
# id2=id(rec)
# print(id2)
# print(id1==id2)


A = {"x": 20, "y": 10, "z": 30}

min_key = min(A, key=A.get)
min_value = A[min_key]

print(min_key, min_value)






