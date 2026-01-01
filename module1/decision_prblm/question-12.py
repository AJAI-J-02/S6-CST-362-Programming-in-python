'''
An electric distribution company charges its domestic consumers as follows
consumption in units     Rate of charge
0-200                       Rs. 0.50 per unit
201 - 400                   Rs. 100 plus rs.0.65 per unit excess of 200
401 -600                    Rs.230 plus Rs.0.80 per unit excess of 400
Above 600                   Rs.425 plus Rs. 1.25 per unit excess of 600
'''



units = float(input("Enter units consumed: "))

if units <= 200:
    bill = units * 0.50
elif units <= 400:
    bill = 100 + (units - 200) * 0.65
elif units <= 600:
    bill = 230 + (units - 400) * 0.80
else:
    bill = 425 + (units - 600) * 1.25

print("Electricity bill: Rs.", bill)


'''
output

Enter units consumed: 450
Electricity bill: Rs. 270.0

'''