# Write a Python program to print first N terms of an arithmetic progression
a=int(input("enter the first number :"))
d=int(input("ener the difference : "))
n=int(input("enter the  terms :"))

for i in range(n):
    print (a+i*d)


# output

# enter the first number :1
# ener the difference : 3
# enter the  terms :10
# 1
# 4
# 7
# 10
# 13
# 16
# 19
# 22
# 25
# 28
