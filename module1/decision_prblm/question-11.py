#. Check whether a number is 3-digit or not
num = input("enter the number :")

if len(num) ==3 and num.isdigit():
    print ("is 3 digit number ")
else:
    print ("not a 3 digit ")


'''

output

enter the number :123
is 3 digit number 



enter the number :abc
not a 3 digit 

'''