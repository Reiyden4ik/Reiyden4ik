import math

class Derivate:
    def __init__(self, f):
        self.__f = f
    
    def __call__(self, x, dx=0.000000001):
        return(self.__f(x+dx) - self.__f(x))/dx
    
@Derivate

def e(x):
    return math.exp(x)


print(e(0))