#Swap 2 numbers without using a temporary variable.
num1=int(input("enter the num1 :"))
num2=int(input("enter the num2 :"))

num1,num2=num2,num1
print("after swap num1 :",num1,"\t num2 :",num2)


#output
# enter the num1 :30 
# enter the num2 :16
# after swap num1 : 16     num2 : 30
