""" input=8
total = 8x9/2 = 36
√36 = 6 ✅"""

import math

def pivotInteger(n: int) -> int:
    total = n * (n + 1) // 2
    x = int(math.isqrt(total))
    
    if x * x == total:
        return x
    return -1


while True:
    n=int(input("Enter number:"))
    x=pivotInteger(n)
    print(x)