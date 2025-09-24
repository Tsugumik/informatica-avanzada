import numpy as np

def estimate_pi(sample_size):
    # Generate a sample_size number of random x and y coordinates between 0 and 1
    # This creates a 2D array (sample_size rows, 2 columns)
    points = np.random.rand(sample_size, 2)

    # Calculate the distance squared from the origin (0,0) for each point
    distances_squared = np.sum(points ** 2, axis=1)

    # Count how many points are inside the circle
    # This creates a bool array
    points_inside_circle: int = np.sum(distances_squared <= 1)

    # Calculate the estimate of Pi
    # The ratio of areas is: (points inside) / (total points) = pi / 4
    # Therefore, pi is estimated as 4 * (ratio)
    pi_estimate = 4 * (points_inside_circle / sample_size)

    return pi_estimate

size = 10000000
pi = estimate_pi(size)

print(pi)