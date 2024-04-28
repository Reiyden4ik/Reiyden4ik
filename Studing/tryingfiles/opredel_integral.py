from sympy import symbols, integrate
import math
# Define the variable
x = symbols('x')
t = symbols('t')

# Define the function
f = (math.cos(t*t))

# Find the integral
F = integrate(f, t)

# define the limits of integration
a = float(input())
b = float(input())

# Evaluate the integral
f_integral = F.subs({x: b}) - F.subs({x: a})    # .subs() is used to substitute the value of x in the function

# Print the result
print("The integral of the function is:", f_integral, F)