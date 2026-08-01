from functools import reduce
#map()
# map() is used to apply the same function to every element in an iterable (such as a list, tuple, or set).
l=[1,2,3,4,5]
square=lambda x:x*x
sqList=map(square,l)
print(list(sqList))
#filter()
# filter() is used to select elements from an iterable that satisfy a given condition. 
# It returns a filter object (iterator) containing only the elements for which the function returns True.
def Is_Even(n):
    if n%2==0:
        return True
    return False
#reduce()
# reduce() combines all elements into a single value using a given function.
onlyEven=filter(Is_Even,l)
print(list(onlyEven))
#reduce
Sum=lambda x,y:x+y
print(reduce(Sum,l))

multi=lambda x,y:x*y
print(reduce(multi,l))