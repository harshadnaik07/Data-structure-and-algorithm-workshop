# name = "harshad"

# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15]) erroe string index out of range 
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:7:2])
# print(name[::-1])


# s= "Python is a High Level programming language"

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

print("subject marks :")
math = 50
chem =  60
phy = 70

print("physics{} chemistry={} math={}".format(phy,chem, math))
print("physics{0} chemistry={1} math={2}".format(phy,chem,math))
print("physics{x} chemistry={y} math={z}".format(x=phy,y=chem,z= math))

total = phy+chem+math

print("total marks",f"{total}")
print("Roll no =","77".zfill(4))




