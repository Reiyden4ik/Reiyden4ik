from sympy import symbols, integrate

# Define the variable
x = symbols('x')

# Define the function
f = (1+x**3)

# Find the integral
F = integrate(f, x)

# define the limits of integration
a = float(input())
b = float(input())

# Evaluate the integral
f_integral = F.subs({x: b}) - F.subs({x: a})    # .subs() is used to substitute the value of x in the function

# Print the result
print("The integral of the function is:", f_integral, F)