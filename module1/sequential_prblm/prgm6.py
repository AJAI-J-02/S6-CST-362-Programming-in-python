#Area and perimeter of a triangle ( p=a+b+c, a=sqrt(s(s-a)s-b)(s-c))
import  math

a=int(input("enter the sides a :"))
b=int(input("enter the side b :"))
c=int(input("enter the sides c :"))

p=a+b+c
s=p/2
a=math.sqrt(s*(s-a)*(s-b)*(s-c))

print ("area",a)
print ("perimeter",p)