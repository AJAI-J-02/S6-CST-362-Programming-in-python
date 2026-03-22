
def _min_max(nums): 
     s=min(nums)
     l=max(nums)
     return s,l
    
    
num=[1,29, 30, 40]

mn,max=_min_max(num)

print("smallest ",mn)
print("largest ",max)
