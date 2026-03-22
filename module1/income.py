income=int(input("enter the income : "))
if income<= 250000:
    tax=0
    print(" zero tax included ")
elif income <= 500000 :
    tax=(income-250000)*0.05
    print(f"tax :{tax}")
elif income<=1000000 :
    tax=12500+(income-500000)*(0.1)
    print(f"tax :{tax}")
elif income> 1000000 :
    tax=62500+(income-1000000)*(0.2)
    print(f"tax :{tax}")