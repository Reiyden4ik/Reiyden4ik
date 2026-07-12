import numpy as np

def divergence(field, dx):
    """
    Calculate the divergence of a vector field.

    Parameters:
    field (numpy.ndarray): A 2D array representing the vector field. The first axis corresponds to the x-coordinate and the second axis corresponds to the y-coordinate.
    dx (float): The spacing between the grid points in the x-direction.

    Returns:
    numpy.ndarray: A 1D array representing the divergence of the vector field.
    """
    return np.gradient(field, dx, axis=0) + np.gradient(field, dx, axis=1)

# Example usage:
field = np.array([[1, 2], [3, 4]])
dx = 1
div = divergence(field, dx)
print(div)