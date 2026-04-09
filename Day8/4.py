import re 


a = input("enter string to perform match operation:")
f =  open("note.txt","r")
c =f.read()
mtch= re.search(a,c)
print(mtch)
if mtch!=None:
    print("match found begining level")
    print(mtch.start()," ",mtch.end())
else:
    print("there is no matching at begining level ")

