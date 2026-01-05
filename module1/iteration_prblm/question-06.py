# . Write a Python program to print even numbers from a starting number to an ending number
s=int(input("enter the starting number :"))
end=int(input("enter the ending number :"))
for i in range(s,end+1):
    if i%2==0:
        print (i)


# out put

# enter the starting number :1
# enter the ending number :10
# 2
# 4
# 6
# 8
# 10
