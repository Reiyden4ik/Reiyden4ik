import numpy as np

def newton_leibniz(f, a, b, n):
    """
    Calculate a definite integral using the Newton-Leibniz formula.

    Parameters:
    f (function): A function to integrate.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of points to use in the trapezoidal rule.

    Returns:
    float: The approximate value of the definite integral.
    """
    # Calculate the step size
    h = (b - a) / n

    # Calculate the x-coordinates of the points
    x = np.linspace(a, b, n + 1)

    # Calculate the y-coordinates of the points
    y = f(x)

    # Calculate the definite integral using the trapezoidal rule
    integral = 0.5 * h * (y[0] + 2 * sum(y[1:-1]) + y[-1])

    return integral

# Example usage:
def f(x):
    return x**2

a = 0
b = 2
n = 1000
integral = newton_leibniz(f, a, b, n)
print("Definite integral:", integral)