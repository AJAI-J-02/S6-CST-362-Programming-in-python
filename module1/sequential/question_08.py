#Swap 2 numbers using a temporary variable
num1=int(input("enter the num1 :"))
num2=int(input("enter the num2 :"))
temp=0
temp=num1
num1=num2
num2=temp
print("after swap num1 :",num1,"\t num2 :",num2)

#output
# enter the num1 :10
# enter the num2 :5
# after swap num1 : 5      num2 : 10
