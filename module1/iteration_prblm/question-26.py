# Find the sum of the series 1 + x +(x^2/2!)+(x^3/3!)+.....+x^n/n!

n=int(input("enter the value :"))
x=int(input("enter the value of x: "))
fact=1
p=1
sum=1
for i in range(1,n+1):
    p=p*x
    fact=fact*i
    sum+=p/fact
print("sum of the series is : ",sum)



"""
output

enter the value :3
enter the value of x: 2
sum of the series is :  6.333333333333333

"""