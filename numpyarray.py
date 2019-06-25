# Ways of creating array
# 1-
from numpy import *

# in numpy no type needed
# arr = array([3,4,5,6,6])


# to declare type
# arr = array([3,4,5,6,6], int)
#
# print(arr)
# print(arr.dtype)
# 2- linspace ()

# initial, to what number, parts, if you dont mention the part it will take 50 by default
# arr = linspace(0,16, 20)
# print(arr)

# 3- arange()
# initial, to what number, steps
# arr = arange(0,16, 2)
# print(arr)
# 4-logspace()
# has the log of the numbers
# arr = logspace(0,16, 2)
# print(arr)
# 5-zeros()
# arr = zeros(6)
# print(arr)
# 6-ones()
# arr = ones(2)
# print(arr)


# zeros and ones give output in float
# if u want int - ones(2, int)
