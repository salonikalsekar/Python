
# overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a= None,b=None, c=None):

        if(a != None and b!= None and c!= None):
            ans =  a + b + c
        elif a!=None and b!= None:
            ans= a +b
        else:
            ans = a
        return ans

# we can also use multiple input *



s1 = Student(50,70)
s2 = Student(90,80)

print(s1.sum(7))

# overriding

class A :
    def show(self):
        print("showing class A")

class B(A):
    def show(self):
        print("showing class B")

# a1= A()
# a1.show()

b1 = B()
b1.show()
# b overrides the show method thats in A