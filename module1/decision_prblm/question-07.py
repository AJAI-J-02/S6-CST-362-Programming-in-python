'''
Write a Python program that takes a single character as input from the user and checks if it is
a vowel or a consonant. If the input is not an alphabetic character, print ”Invalid input.”
'''

char=input("enter the character :")
if not char.isalpha():
    print ("invalid enter a string ")
elif char in "aeiouAEIOU":
    print ("is vowels ")
else:
    print ("is consonant")

'''
output

enter the character :a
is vowels 

enter the character :y
is consonant


enter the character :5
invalid
'''

