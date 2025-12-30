#Area and perimeter of a triangle ( p=a+b+c, a=sqrt(s(s-a)s-b)(s-c))
import  math

a=int(input("enter the value a :"))
b=int(input("enter the value b :"))
c=int(input("enter the value c :"))

p=a+b+c
s=p/2
a=math.sqrt(s*(s-a)*(s-b)*(s-c))

print ("area",a)
print ("perimeter",p)



#out put
# enter the value a :3
# enter the value b :4
# enter the value c :5
# area 6.0
# perimeter 12
