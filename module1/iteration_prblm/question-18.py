# Find the sum of digits of a number
n=int(input(" enter the number :"))
sum=0
while n>0:
    temp=n%10
    sum=sum+temp
    n=n//10


print(sum)

"""
output

 enter the number :12
    3

"""