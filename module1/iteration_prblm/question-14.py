# Check whether a number is amstrong or not

num=int(input("enter the number "))
sum=0
temp=num
digits=len(str(num))
while temp>0:
    digit =temp%10
    sum=sum+digit ** digits
    temp//=10
if sum==num :
    print(num,"is amstrong")
else:
    print(num,"is not amstrong" )

# output

# enter the number 153
# 153 is amstrong

