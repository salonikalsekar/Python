# Problem Description
# The program takes both the values from the user and swaps them without using temporary variable.

# Problem Solution

x = int(input("Enter first value: "))
y = int(input("Enter second value: "))

x , y = y,x
print(x ,y)


# Time complexity -> O(1)