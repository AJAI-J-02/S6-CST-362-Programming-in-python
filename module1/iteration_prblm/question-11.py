# Print the fibonacci series
n=int(input(" enter a number :"))

a,b=0,1

print("Fibonacci series:")

for i in range(n):
    print(a)
    a, b = b, a+b


# out put

#  enter a number :7
# Fibonacci series:
# 0
# 1
# 1
# 2
# 3
# 5
# 8