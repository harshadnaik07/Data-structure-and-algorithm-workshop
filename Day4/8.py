import csv
f= open("students.csv","a",newline="")
a=csv.writer(f)
# a.writerow(['rollno','name','mobile no',"p1","p2","p3","total","percentage","email","result"])


rollno=int(input("enter roll no :"))
name=input("enter name :")
mobile_no=int(input("enter mobile no :"))
p1=int(input("enter marks for p1:"))
p2=int(input("enter marks for p2:"))
p3=int(input("enter marks for p3:"))
total= p1+p2+p3
percentage=total/3
email=input("enter your email:" )
if percentage>=40:
    result="pass"
else:
    result="fail"

a.writerow([rollno,name,mobile_no,p1,p2,p3,total,percentage,email,result])
print("student record has saved")