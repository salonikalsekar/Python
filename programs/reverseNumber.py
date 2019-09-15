# Problem Description
# The program takes a number and reverses it.

# Problem Solution

n  = int(input('Enter the number'))
newReverse = 0


if n< 0:
    sign = -1
else:
    sign = 1
    
n = sign * n

while n > 0:
    newReverse =  newReverse * 10 + n%10 
    n = n // 10

print(newReverse * sign)

# time complexity O(n)