# instance methods
# static methods
# class methods

class Student:

    school = 'ptv'
    def __init__(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3


    def averageMarks(self):
        return (self.marks1 + self.marks2 + self.marks3)/3


# class method working with class variable
    @classmethod
    def getValue(cls):
        return cls.school

    @staticmethod
    def info():
        print("static method")



s1 = Student(22,40,55)

s2 = Student(66,78,90)

print(s1.averageMarks())
print(s2.averageMarks())

print(Student.getValue())


Student.info()

# Accessors: get the values
# mutators: set the values - change the values
# static methods are not concerned about class or instance variables
