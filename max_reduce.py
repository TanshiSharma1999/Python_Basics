from functools import reduce
a=[123,2,29,78,33,900,99]
def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,a))

