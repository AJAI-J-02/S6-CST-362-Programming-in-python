# Check whether a number is perfect number or not
n=int(input("enter the number "))
sum=0
for i in range(1,n):
    if n%i==0:
        print(i)
        sum=sum+i

if sum==n:
    print ("is perfect number ")
else :
    print ("is not perfect number")

#output
# enter the number 6
# 1
# 2
# 3
# is perfect number 

