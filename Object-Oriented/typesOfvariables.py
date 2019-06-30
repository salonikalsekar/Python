# there are 2 types of variables - class variables and instance variables

class Car:

    b = "class_variable"
    def __init__(self):
        self.a = 15



c1 = Car()
c2 = Car()

c1.a = 8

print(c1.a, c1.b)
print(c2.a, c2.b)

# a is an instance variable
# b is a class variable