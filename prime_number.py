# check if prime using for_else

num = 10
#
# for i in range(2, num):
#     if num % i == 0:
#         print("Not prime")
#         break
#
# else:
#     print("Prime")


# for efficiency we can run it till the half loop

for i in range(2, num//2):
    if num % i == 0:
        print("Not prime")
        break

else:
    print("Prime")