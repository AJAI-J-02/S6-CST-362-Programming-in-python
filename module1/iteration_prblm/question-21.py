# Find the sum of odd digits in a number

n=int(input("enter the number :"))
sum=0
while n!=0:
    temp=n%10
    if n%2!=0:
        sum=sum+temp
    n=n//10
print ("the sum of odd digits are :",sum)

"""

output

enter the number :235
8


"""