from array import *

newarray = array('i', [4,5,6,7,8])
# for char we use typecode u - unicodes
# address and length of an array

# if you dont know the type

newValuedArray = array(newarray.typecode, (a for a in newarray))
# print(newarray.buffer_info())
#
# print(newarray)
#
# print(newarray.typecode)
#
# newarray.reverse()
#
# print(newarray)
#
# print(newarray[3])
#
# for i in range(5):
#     print(newarray[i])
#
# for i in newarray:
#     print(i)

print(newValuedArray)


# we can also use while loop
i=0
while i< len(newValuedArray):
    print(newValuedArray[i])
    i+=1