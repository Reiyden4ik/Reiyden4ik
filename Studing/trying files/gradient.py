import numpy as np

def nabla(f, dx, dy, dz):
    """
    Calculate the gradient of a scalar function in 3D space using the nabla operator.

    Parameters:
    f (numpy.ndarray): A 3D array representing the scalar function. The first axis corresponds to the x-coordinate, the second axis corresponds to the y-coordinate, and the third axis corresponds to the z-coordinate.
    dx (float): The spacing between the grid points in the x-direction.
    dy (float): The spacing between the grid points in the y-direction.
    dz (float): The spacing between the grid points in the z-direction.

    Returns:
    numpy.ndarray: A 3D array representing the gradient of the scalar function. The first axis corresponds to the x-component of the gradient, the second axis corresponds to the y-component of the gradient, and the third axis corresponds to the z-component of the gradient.
    """
    return np.gradient(f, dx, axis=0), np.gradient(f, dy, axis=1), np.gradient(f, dz, axis=2)

# Example usage:
f = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
dx = 1
dy = 1
dz = 1
grad = nabla(f, dx, dy, dz)
magnitude = np.sqrt(grad[0]**2 + grad[1]**2 + grad[2]**2)
print("Gradient magnitude:", magnitude)