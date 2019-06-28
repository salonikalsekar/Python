class Computer:
    def __init__(self, cpu):
        self.cpu = cpu
        print("hello from init")


    def config(self):
        print("something ", self.cpu)

#
# com1 ="sasa"
#
# Computer.config(com1)


com = Computer('33')

com.config()


# com takes some space in heap memory
# everytime you create an object it creates a new space