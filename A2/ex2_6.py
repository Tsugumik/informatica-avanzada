from ex2_2 import Point2D
from ex2_3 import generate_random_points
from ex2_5 import line_from_points
import numpy as np
import matplotlib.pyplot as plt


def random_line(p1, p2):
    points_generator = generate_random_points(p1, p2, 2)
    p_rand1 = next(points_generator)
    p_rand2 = next(points_generator)

    return line_from_points(p_rand1, p_rand2)

if __name__ == "__main__":
    vertex1 = Point2D(-1, -1)
    vertex2 = Point2D(1, 1)

    num_lines = 5

    plt.figure(figsize=(8, 8))

    rect_x = [vertex1.x, vertex2.x, vertex2.x, vertex1.x, vertex1.x]
    rect_y = [vertex1.y, vertex1.y, vertex2.y, vertex2.y, vertex1.y]
    plt.plot(rect_x, rect_y, 'r--', label='Rectangle Boundary')

    x_values = np.linspace(-10, 10, 100)
    for i in range(num_lines):
        try:
            random_line_eq = random_line(vertex1, vertex2)
            y_values = random_line_eq.get_y(x_values)
            plt.plot(x_values, y_values, alpha=0.7, label=f'Random Line {i + 1}')
        except ValueError:
            print("A vertical line was generated and will not be plotted.")

    plt.title(f"{num_lines} Random Lines Crossing a Rectangle")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()