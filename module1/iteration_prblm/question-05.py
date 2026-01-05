# . Find the sum of odd numbers in a set of N numbers
n=int(input(" enter the set of number :"))
sum=0
for i in range(n):
    num=int(input("enter the number "))
    if num%2!=0:
        sum=sum+num

print ("sum of ood numers are :",sum)



# output

# enter the set of number :5
# enter the number 1
# enter the number 3
# enter the number 2
# enter the number 4
# enter the number 5
# sum of ood numers are : 9
