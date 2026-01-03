# Check whether a number is prime or not
n=int(input("enter the number "))
if n<=1:
    print("is not a prime ")

else:

    for i in range (2,n):
        if n%i==0:
            print ("is not prime ")
            break
    else:
        print ("is prime ")

#out put

# enter the number 2
# is prime 



