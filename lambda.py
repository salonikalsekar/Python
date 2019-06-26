

def mult(a,b):
    c = a * b
    return c

ans = mult(4,5)
print(ans)

#  sometimes we have only one line to return, then why to waste 2 lines in defining and calling functions
# Anonymous functions
f = lambda a,b : a * b

result = f(4,5)
print(result)