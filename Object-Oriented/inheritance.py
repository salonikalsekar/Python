class A:

    def __init__(self):
        print("init A")

    def feature(self):
        print("feature1 class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("init B")

    def feature1(self):
        print("feature 2 class B")

class C(B):
    def __init__(self):
        super().__init__()
        print("init C")

    def feature2(self):
        print("feature 3 class c")

a1 = A()
b1 = B()
c1 = C()

# a1.feature()
# b1.feature1()
# b1.feature()
# c1.feature2()


# class B is inherting features from class A
# class A is super class
# class B is subclass

# we use super() keyword to access constructor or any of the parent class features
# MRO-  method resolution order is always from left to right - for multi level inheritance
