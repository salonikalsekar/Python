a = 5
b = 6


print(a + b)

print(int.__add__(a, b))
# we have str.__add__ as well

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 =  other.m1 + self.m1
        m2 = other.m2 + self.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 =  other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

s1 = Student(50,70)
s2 = Student(90,80)

s3 = s1 + s2

print(s3.m2)

print(s1 > s2)