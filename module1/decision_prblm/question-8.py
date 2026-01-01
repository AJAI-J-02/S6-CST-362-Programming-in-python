'''
Write a Python program that checks the strength of a password entered by the user. The
program should categorize the password as: ”Weak” if it is less than 6 characters. ”Medium”
if it is between 6 and 10 characters. ”Strong” if it is more than 10 characters
'''
pswd=input("enter the passward :")
l=len(pswd)

if l<6:
    print (" password is weak ")
elif 6<l<10:
    print (" medium")
else:
    print ("is strong..")

'''
output

enter the passward :AJAI
 password is weak 

enter the passward :1234567
 medium

enter the passward :123456789a
is strong..

'''