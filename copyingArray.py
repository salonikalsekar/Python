from numpy import *



arr1 =  array([3,4,5,6,6])
arr2 = array([33,4,5,66,7])

#adding element to all elements
arr = arr1 + 3

print(arr)

#vectorized operation- adding two arrays
arr3 = arr1 + arr2
print(arr3)

# max()
# sort()
# unique()
# concatenate(a1, a2)
# This is also called aliasing
# copying an array
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr2))
print(id(arr1))
# both have same address

# If you want 2 addresses
arr2 = arr3.view()
print(arr2)
print(id(arr2))
print(id(arr3))

# There are two types of copying: shallow and deep
# Shallow is - it will copy but any change in any one will change the other array
# Example:

arr2[1]= 3
print(arr2)
print(arr3)

# Deep is - it will copy but any change in any one wont change the other array
# For that we use copy
# Example:

arr2 = arr1.copy()
print(arr2)
print(arr1)
print(id(arr2))
print(id(arr1))
arr2[3] = 00
print(arr2)
print(arr1)