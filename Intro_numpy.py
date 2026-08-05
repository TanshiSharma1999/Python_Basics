import numpy as np

print("First Numpy Program")
print("*"*50)
a=np.array([1,2,3])
b=np.array([4,5,6])
print("Array 1=",a)
print("Array 2=",b)
print("Sum of the two: ",a+b)
print("Product of the two: ",a*b)
print("Difference of the two: ",a-b)
print("Quotient of the two: ",a/b)


print("*"*50)
arr1=np.array([[2.0,3.0,4.0],[1.0,2.0,3.0]])
print(arr1)
print(arr1.ndim)#tell how many dimentions
print(arr1.shape)#rows ,columns
print(a.dtype)

a2=np.array([1,2,3],dtype="int16")
print(a2.dtype)#you can specify a size also

#shows byte size
print(a.itemsize)
print(a2.itemsize)
#a has 3 items of each 8bytes itemsize
print(a.nbytes)#24
#a2 has 3 items of each 2bytes itemsize
print(a2.nbytes)#6
