# if statements
# r=2
#
# if r==0:
#     print("Even")
# elif r==1:
#     print("odd")
# elif r==2:
#     print("true")


# while loop

#
# i = 6
#
# while i <=6:
#     print("sal", i)
#     i =+1

# for loop

newlist= [1,4,5,6,7,8]

# for i in [4,5,6,7]:
#     print(i)
# for i in newlist:
#     print(i)
# for i in range(2,21,3):
#     print(i)


# break continue pass
for i in range(11):
    if i % 3 ==0 or i% 5==0:
        continue
    else:
        print(i)


# break is coming out of the loop completely
# pass is just ignoring the block and continuing with the remaining code in the current loop
# continue is forcefully exiting from the loop and starting the next loop