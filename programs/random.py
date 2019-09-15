# https://www.sanfoundry.com/python-problems-solutions/ - simple questions starting from question 6
# l = [5,6,7,8,9]
# n1 = int(input('Enter the number'))
n2 = int(input('Enter the second number'))
# n3  = int(input('Enter a 3 digit number'))
# n4  = int(input('Enter a 4 digit number'))
# numRow = int(input('Enter number of rows'))
# numCol= int(input('Enter number of columns'))
# palindromNum  = int(input('Enter s number for checking palindrome '))

# print("Question 6")
# print("Marks: ", sum(l)// 5)

# print("Question 7")
# for i in range(10):
#     if i%n2 == 0:
#         print(i)


# print("Question 8")

# print(n1 // n2, n1 % n2)

# print("Question 9")

# print("Question 10")

# for i in range(10):
#     if i%2  != 0 :
#         print(i)

# print("Question 11")
# total = 0
# while n3 > 0:
#     ans = n3 %10
#     total = total + ans
#     n3 = n3 // 10
# print(total)


# print("Question 12")
# arr=[]
# for i in range(2, n2 + 1):
#     if n2 % i == 0:
#         arr.append(i)

# arr.sort()
# print("Smallest divisor", arr[0])

# print("Question 13")
# c= 0

# while n4 != 0:
#     c += 1
#     n4 = n4//10

# print(c)


# print("Question 14")
# reverseNum = 0
# dig = palindromNum
# while dig != 0:
#     reverseNum = dig % 10 + reverseNum *10
#     dig = dig // 10

# if palindromNum == reverseNum:
#     print("is a palindrome")
# else:
#     print("not a palindrome")

# print("Question 15")
# for i in range(1,51):
#     if i % 2 != 0 and i%3 != 0:
#         print(i)
# print("Question 16")

sum = 0
seq = ""
for i in range(n2):
    sum = sum + i
    seq = seq + str(i) + " "

print(seq + "  =",  str(sum))
# print("Question 17")
# print("Question 18")
# for s1 in range(n2):
#     for s2 in range(n2):
#         if s1 == s2:
#             print(1, sep=" ", end= " ")
#         else:
#             print(0, sep=" ", end= " ")
# print("Question 19")
# # for r in range(numRow):
# #     for c in range(r, numCol):
# #         print("*", end = '')
# #     print('/n')
    
# print("Question 20")

