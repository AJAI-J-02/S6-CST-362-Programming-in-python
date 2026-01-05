# Print the following different patterns
rows = int(input(" enter the rows "))

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

'''

output

 enter the rows 5
    *
   ***
  *****
 *******
*********
'''