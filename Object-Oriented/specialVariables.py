print (__name__)

# the first module name is always main -  this is the start point of execution

# for the modules which are not the point of execution - it will print the module name


class Design:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        print("constructor called")

    def printingFunc(self):
        print("dimensions are", self.dimensions)



val = Design(13)


val.printingFunc()


