#Print the amstrong numbers between 2 limits

num1=int(input("enter start number :"))
num2=int(input("enter the end limit : "))

for num in range (num1,num2+1):
    temp=num

    sum=0

    digits=len(str(num))
    while temp>0:
        digit =temp%10
        sum=sum+digit ** digits
        temp//=10
    if sum==num :
        print(num,"is amstrong")

# output
# enter start number :100
# enter the end limit : 1000

# 153 is amstrong
# 370 is amstrong
# 371 is amstrong
# 407 is amstrong