# Find the difference between the sum of odd digits and even digits in a number
n=int(input("enter the number :"))
sum=0
sum1=0
while n!=0:
    temp=n%10
    if n%2!=0:
        sum=sum+temp
    elif n%2==0:
        sum1=sum1+temp
    n=n//10

    dif=sum-sum1
print ("the sum of odd digits are :",sum," and summ of even digits ",sum1)
print ("the sum of odd digits are :",dif)

'''

output

enter the number :12345
the sum of odd digits are : 9  and summ of even digits  6
the sum of odd digits are : 3

'''