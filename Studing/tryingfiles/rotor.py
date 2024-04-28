import numpy as np

def rotor(field, dx, dy, dz):
    """
    Calculate the rotor (curl) of a vector field in 3D space.

    Parameters:
    field (numpy.ndarray): A 3D array representing the vector field. The first axis corresponds to the x-coordinate, the second axis corresponds to the y-coordinate, and the third axis corresponds to the z-coordinate.
    dx (float): The spacing between the grid points in the x-direction.
    dy (float): The spacing between the grid points in the y-direction.
    dz (float): The spacing between the grid points in the z-direction.

    Returns:
    numpy.ndarray: A 3D array representing the rotor (curl) of the vector field. The first axis corresponds to the x-component of the rotor, the second axis corresponds to the y-component of the rotor, and the third axis corresponds to the z-component of the rotor.
    """
    return np.gradient(field[:, :, 2], dx, axis=0) - np.gradient(field[:, :, 0], dz, axis=2), \
           np.gradient(field[:, :, 0], dy, axis=1) - np.gradient(field[:, :, 1], dx, axis=0), \
           np.gradient(field[:, :, 1], dz, axis=2) - np.gradient(field[:, :, 2], dy, axis=1)

# Example usage:
field = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
dx = 1
dy = 1
dz = 1
rot = rotor(field, dx, dy, dz)
print("Rotor (curl):", rot)