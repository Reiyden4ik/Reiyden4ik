from sympy import symbols, diff

# Define the variable
x = symbols('x')

# Define the function
f = x**2 + 2*x + 1 + x**3

# Find the derivative
f_prime = diff(f, x)

# Print the result
print("The derivative of the function is:", f_prime)