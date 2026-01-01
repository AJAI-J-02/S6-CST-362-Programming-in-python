#Find the largest of 3 numbers
n1=int(input("enter the 1st number :"))
n2=int(input("enter the 2nd number :"))
n3=int(input("enter the 3rd number :"))

if n1>n2 and n1>n3:
    print (n1,"is greater ")
elif n2>n1 and n2>n3:
    print (n2,"is greater ")
elif n3 > n1 and n3 > n2:
    print(n3, "is greater")
else:
    print("some of entered numbers are equal ")


'''
output

enter the 1st number :5
enter the 2nd number :8
enter the 3rd number :1
8 is grater

'''