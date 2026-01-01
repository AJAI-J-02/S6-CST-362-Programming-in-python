#Find the large digit in a two-digit number
num1=int(input("enter the number :"))
temp=num1%10
temp2=num1//10
if temp>temp2:
    print ("second number is greater :",temp)
elif temp==temp2:
    print("both number same enter a different  ")
else:
    print("first number is greater :", temp2)


"""
out put

enter the number :82
first number is greater : 8

"""
