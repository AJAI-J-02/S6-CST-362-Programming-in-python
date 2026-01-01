#Check whether a number is completely divisible by another number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % num2 == 0:
    print(num1, "is completely divisible by", num2)
else:
    print(num1, "is NOT completely divisible by", num2)


#out put
# Enter the first number: 24
# Enter the second number: 3
# 24 is completely divisible by 3


# Enter the first number: 5
# Enter the second number: 3
# 5 is NOT completely divisible by 3
