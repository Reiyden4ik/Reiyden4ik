import math

class Derivate:
    def __init__(self, func):
        self.__fn = func
    
    def __call__(self, x, dx=0.000000001):
        return(self.__fn(x+dx) - self.__fn(x))/dx

class ixina:
    def __init__(self, x, a):
        self.__x = x
        self.__a = a
    def __call__(self, x, dx=0.000000001):
        return(self.__fn(x+dx) - self.__fn(x))/dx

@Derivate
def expanenta(x):
    return math.exp(x)

print(expanenta(0))