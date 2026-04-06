import csv
f= open("student.csv","a",newline="")
a=csv.writer(f)
# a.writerow(['studentID','rollno','name','mobile no'])

studentID=int(input("enter student id :"))
rollno=int(input("enter roll no :"))
name=input("enter name :")
mobile_no=int(input("enter mobile no :"))

a.writerow([studentID,rollno,name,mobile_no])
print("student record has saved")