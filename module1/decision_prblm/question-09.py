#Determine the nature of the solution of the quadratic equation
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = b*b - 4*a*c

if D > 0:
    print(" real and distinct roots")
elif D == 0:
    print(" real and equal roots")
else:
    print("No real roots ")

'''
output

Enter a: -20
Enter b: 2
Enter c: 4
 real and distinct roots

'''