#Convert the seconds to hours : minute : seconds
sec=int(input("enter the second :"))
hour=sec//3600
minute=(sec%3600)//60
seconds=sec%60
print("\n hour :",hour,"\n minute",minute,"\n seconds :",seconds)