from array import *

arr = array('i', [])

# insert into array
n = int(input('Enter the length of the array'))

for i in range(n):
    x = int(input('Enter the value of the array'))
    arr.append(x)

print(arr)

val = int(input('Enter the value to search'))

k=0
for i in arr:

    if i==val:
        print(k)
        break

    k += 1

# print(arr.index(val))