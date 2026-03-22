my_data={'b':20,'a':35}
my_data['b']=22# for upadte just assign new value with key in square bracket
my_data['b']=-my_data['b']  # nagtion

my_data['c']=40 # just add simply

my_data.pop('b',None)# pop for delete


# print(my_data['b'])# can access value by giving inside square bracket
print(my_data)

print(sorted(my_data))
