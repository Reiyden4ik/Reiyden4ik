from sympy import symbols, limit, sin, oo
import math

# Define the variable of the function
x = symbols('x')

# Define the function
f = sin(x)

# Calculate the limit of the function as x approaches 0 from the left
left_limit = limit(f, x, (math.pi)/2, dir='-')

# Calculate the limit of the function as x approaches 0 from the right
right_limit = limit(f, x, (math.pi)/2, dir='+')

# Print the limits
print("Left limit:", left_limit)
print("Right limit:", right_limit)