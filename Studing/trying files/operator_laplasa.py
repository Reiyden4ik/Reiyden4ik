import numpy as np

def laplacian(f, dx, dy, dz):
    """
    Calculate the Laplacian of a scalar function in 3D space.

    Parameters:
    f (numpy.ndarray): A 3D array representing the scalar function. The first axis corresponds to the x-coordinate, the second axis corresponds to the y-coordinate, and the third axis corresponds to the z-coordinate.
    dx (float): The spacing between the grid points in the x-direction.
    dy (float): The spacing between the grid points in the y-direction.
    dz (float): The spacing between the grid points in the z-direction.

    Returns:
    numpy.ndarray: A 3D array representing the Laplacian of the scalar function.
    """
    return np.gradient(np.gradient(f, dx, axis=0), dy, axis=1) + np.gradient(np.gradient(f, dy, axis=1), dz, axis=2)

# Example usage:
f = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
dx = 1
dy = 1
dz = 1
lap = laplacian(f, dx, dy, dz)
print("Laplacian:", lap)