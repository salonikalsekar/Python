# Problem Description
# The program takes the elements of the list one by one and displays the average of the elements of the list.

# Problem Solution


n  = int(input("Enter the total number: "))
arr = []

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)

ans = sum(arr) / n
print(sum(arr), n, ans)

# Time complexity -> O(n)