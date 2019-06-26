# In python there is no call by reference nor call by value
# whenever you pass a value to a function, the address the variables will be same. But the moment yuo update it, it refers to a different address

# since strings are immutable, updating a string -referenced to a new address same with int
# but for mutable types like list, wont change the address

def new(x):
    print(id(x))

    x=0

    print(id(x))
    print(x)

a = 9

new(a)

print(id(a))

# 2 types of arguments
# formal arguments-
# def fn(a,b):
#
# fn(a,b

# actual arguments - position, keyword, default,variable length
# position:
# def fn(a,b):
#
# fn(4,5)

# if you dont know the sequence: we use keywords, mention the variable names
# keyword:
# def fn(a,b):
#
# fn(4,5)

# default:
# setting default values
# def fn(a,b="sal")
#
# fn(4)
# if you still pass a value, it will be considered instead of the default one

# Variable length argument:
# * is multiple values and will take it as a tuple.
# def fn(a, *b):
#
# fn(4,5,56,7)

# in this variable length we can face issues that is the function wont know what is it getting, so for that we have keyworded variable length argument

# so  thats when you use **data

# def fn(a, **b:
#now b will be changed to dictionary
#   for i,j in b.items():
#     print(i,j)
# fn(4,age=5, name="sasa", mob="5555")



###################################################

# to refer a global variable we use the keyword-global a
# and to change the global variable we use globals()['a']

# passing list to a function

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd += 1
    return even, odd

lst = [5,6,7,33,4,56,76,88,77,97]

even, odd= count(lst)
print("Even : {} and Odd {}".format(even,odd))

