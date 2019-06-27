# if you want to change the without actually changing the existing function- use decorators

#div function you cant change
def div(a,b):
    print("hello4")
    print(a/b)


def newDiv(func):

    print("hello1")
    def inner(a,b):
        print(a,b)
        print("hello3")
        if a < b:
            a,b = b,a
        return func(a,b)

    print("hello2")
    return inner



div = newDiv(div)

div(2,4)