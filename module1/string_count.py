string=input("enter the string :")
count_dict={}

for ch in string:
    if ch in count_dict:
        count_dict[ch]+=1  #iff present increment the value
    else:
        count_dict[ch]=1 # if not present just add with 1 as value
        
print (count_dict)    
