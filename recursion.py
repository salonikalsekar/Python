import sys

# to set recursion limit
sys.setrecursionlimit(2000)

# to check the limit
print(sys.getrecursionlimit())


count=0
def rec():
    global count
    count+=1

    print("rec", count)
    rec()

# rec()



# finding factorial using recursion
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)



rsult = fact(5)

print(rsult)