from sympy import symbols, integrate

# Define the variable
x = symbols('x')

# Define the function
f = (1+x**3)

# Find the integral
f_integral = integrate(f, x)

# Print the result
print("The integral of the function is:", f_integral)