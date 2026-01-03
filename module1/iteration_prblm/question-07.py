# A Python program to read a number N and print the even numbers in reverse order starting
# from N
n=int(input("enter a n numbers : "))
for i in range(n,-1,-1):
    if i%2==0:
         print(i)


# output

# enter a n numbers : 5
# 4
# 2
# 0