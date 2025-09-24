from ex2_2 import Point2D
import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(p1, p2, n):
    min_x = min(p1.x, p2.x)
    max_x = max(p1.x, p2.x)
    min_y = min(p1.y, p2.y)
    max_y = max(p1.y, p2.y)

    random_x = np.random.uniform(min_x, max_x, n)
    random_y = np.random.uniform(min_y, max_y, n)

    for i in range(n):
        yield Point2D(random_x[i], random_y[i])

if __name__ == "__main__":
    vertex1 = Point2D(-5, -5)
    vertex2 = Point2D(5, 5)
    num_points = 10000

    random_points = generate_random_points(vertex1, vertex2, num_points)

    x_coords = []
    y_coords = []
    for p in random_points:
        x_coords.append(p.x)
        y_coords.append(p.y)

    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, s=5, color='blue', alpha=0.6)

    rect_x = [vertex1.x, vertex2.x, vertex2.x, vertex1.x, vertex1.x]
    rect_y = [vertex1.y, vertex1.y, vertex2.y, vertex2.y, vertex1.y]
    plt.plot(rect_x, rect_y, 'r--', label='Rectangle Boundary')

    plt.title(f"Uniformly Distributed Random Points in a Rectangle ({num_points} points)")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
