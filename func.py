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

