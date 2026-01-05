# Find the sum of the series
# 1 + (1/2)+(1/3) + · · · + (1/n)

n=int(input("enter the valuea :"))
sum=0
for i in range(1,n+1):
    sum=sum+1/i
print("sum of the series is : ",sum)

'''
output

enter the valuea :3
sum of the series is :  1.833333333333333

'''
