# Check whether a number is palindrome or not
n=int(input(" enter the number :"))
temp1=n
rev=0
while n>0:
    temp=n%10
    rev = rev * 10 + temp
    n=n//10


print("revers of number ",rev)
if temp1==rev:
    print("number is palindrom ")
else:
    print("not palindrom ")


'''

output

enter the number :333
revers of number  333
number is palindrom       



'''