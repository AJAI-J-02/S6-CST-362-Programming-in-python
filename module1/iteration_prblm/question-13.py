# Print the prime numbers between the 2 limits
limit1=int(input("enter the limit1  "))
limit2=int(input("enter the limit2 "))

for n in range(limit1,limit2+1):
    if n>1:  
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print (n)
                


# out put

# enter the limit1  2
# enter the limit2 9
# 2
# 3
# 5
# 7

