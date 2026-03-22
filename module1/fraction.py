import math
x=float(input("enter the x :"))
n=int(input("enter the n :"))

sum=0

for i in range(0,n-1):
  
    term=((-1)**i)*(x**(2*i))/math.factorial(2*i)
    
    sum+=term
print("cos(x)=",sum)