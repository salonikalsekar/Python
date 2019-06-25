from numpy import *



arr1 =  array([[3,4,5,6,3,4,5,6],[36, 77,8,9, 66 ,77,66,3]])

print(arr1)

print(arr1.dtype)
print(arr1.ndim)
# rows and colum length
print(arr1.shape)

# total number of elements
print(arr1.size)

# convert 2-d to 1-d array
arr2= arr1.flatten()
print(arr2)

# convert 1-d to 2-d array
# pass rows, columns
arr3= arr2.reshape(4,4)
print(arr3)

# to create a 3d array
# 4 2 d array having 2 elements
arr4= arr2.reshape(4,2,2)
print(arr4)


array1= array([[3,4,5,6,3,4,5,6],[36, 77,8,9, 66 ,77,66,3]])
m = matrix(array1)
# m = matrix('3,4,5,6;67,7,8,85')

print(diagonal(m))
print(m.max())

# to multiply 2 matrices - assume having m1 m2 matrices

m3 = m1 * m2