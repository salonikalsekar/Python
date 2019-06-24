# In python we can do for else

nums = [33,7,67,86,3,9]

# for i in nums:
#     if i % 5 ==0:
#         print(i)
#         break
#     else:
#         print("not found")


# Here we will get not found 5 times, we want it only once so we write else for for not if

for i in nums:
    if i % 5 == 0:
        print(i)
        break
else:
    print("not found")
