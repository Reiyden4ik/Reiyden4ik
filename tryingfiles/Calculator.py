class Calculator:
    def __init__(self):
        self.value = None

    def add(self, x, y):
        self.value = x + y
        return self.value

    def subtract(self, x, y):
        self.value = x - y
        return self.value

    def multiply(self, x, y):
        self.value = x * y
        return self.value

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        self.value = x / y
        return self.value

    def clear(self):
        self.value = None

    def get_value(self):
        return self.value

calculator = Calculator()
print('Введите +, -, *, /')
c = input()
print("Введите 2 числа:")
a = float(input())
b = float(input())
if c == '+':
    calculator.add(a, b)
    print(calculator.get_value())  
if c == '-':
    calculator.subtract(a, b)
    print(calculator.get_value())  
if c == '*':
    calculator.multiply(a, b)
    print(calculator.get_value())  
if c == '/':
    if b == 0:
        try:
            calculator.divide(a, b)
        except ValueError as e:
            print(e)
    else: 
        calculator.divide(a, b)
        print(calculator.get_value())  
