#Set stores immutable(unchangable) items, unique , unordered
nums=[1,2,3,4,5,2]
sample_set=set(nums)
print(sample_set,type(sample_set))
print(nums,type(nums))

l=[]
print(type(l))
s=set()
print(type(s))

myset={1,2,3,4,5,6}
myset.add(8)
print(myset)
myset.remove(1)
print(myset)
#yay
if 8 in myset:
    print("Yay")
else:
    print("Nahh")
#Nahh
if 1 in myset:
    print("Yay")
else:
    print("Nahh")


#Set operation
t={1,2,3,4}
s={4,6,7,8}

print("Union ",t.union(s))
print("Intersection ",t.intersection(s))
print("Difference: ",t.difference(s))
print("Difference: ",s.difference(t))

