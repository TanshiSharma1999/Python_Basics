# Find the maximum and minimum elements in a tuple. without min() and max()
tup=(12,34,5,167,1,23,0,100,111,46)
def max_min_tup():
    min=tup[0]
    max=tup[0]
    for i in tup:
        if i<min:
            min=i
        if i>max:
            max=i

    return min,max

min,max=max_min_tup()
print("tuple=",tup)
print("Minimum=",min)
print("Maximum=",max)
