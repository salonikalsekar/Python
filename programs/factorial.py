

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = i * ans
    print(ans)

fact(5)


# recursion


def factrec(n):
    if n == 0:
        return 1

    else:
        return n * factrec(n-1)

print(factrec(5))