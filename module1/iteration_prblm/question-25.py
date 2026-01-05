# Find the sum of the series 1 + 2/2+2/3!+3/3! + · · · + n/n!
n=int(input("enter the valuea :"))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+i/fact
print("sum of the series is : ",sum)


"""
out put

enter the valuea :3
sum of the series is :  2.5

"""
