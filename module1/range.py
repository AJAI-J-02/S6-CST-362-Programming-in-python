

for i in range(100,1000):
    temp=i
    digit=0
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit
        temp=temp//10
    if sum%3==0:
        print(i,end=" ")
    
    

