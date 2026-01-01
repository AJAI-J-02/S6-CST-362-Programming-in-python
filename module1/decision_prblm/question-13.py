'''
Write a Python program to read percentage of marks scored by a student in an examination
and print the percentage of marks along with the g obtained using the following conditions
(a) percentage ≥ 90 “O(Outstanding)”
(b) percentage ≥ 85 and percentage < 90, “A+ (Excellent)”
(c) percentage ≥ 80 and percentage < 85, “A (Very Good)”
(d) percentage ≥ 70 and percentage < 80, “B+ (Good)”
(e) percentage ≥ 60 and percentage < 70, “B (Above Average)”
(f) percentage ≥ 50 and percentage < 60, “C (Average)”
(g) percentage ≥ 45 and percentage < 50, “P (Pass)”
(h) percentage < 45 “F (Fail)
'''

percentage = float(input("Enter the percentage of marks: "))



if percentage >= 90:
    g = "O (Outstanding)"
elif percentage >= 85:
    g = "A+ (Excellent)"
elif percentage >= 80:
    g = "A (Very Good)"
elif percentage >= 70:
    g = "B+ (Good)"
elif percentage >= 60:
    g = "B (Above Average)"
elif percentage >= 50:
    g = "C (Average)"
elif percentage >= 45:
    g = "P (Pass)"
else:
    g = "F (Fail)"

print("Percentage :",percentage,"%")
print("grade ",g)

