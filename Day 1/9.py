amount = int(input("please enter amount for withdraw:"))

print("100 notes:", amount//100)
print("50 notes:",(amount%100)//50)
print("20 notes:",((amount%100)%50)//20)
print("10 notes:",(((amount%100)%50)%20)//10)
print("5 notes:",((((amount%100)%50)%20)%10)//5)