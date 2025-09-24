from ex2_2 import Point2D
from ex2_3 import generate_random_points
from ex2_4 import LinearEquation
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    line = LinearEquation(a=2, b=-1, c=3)

    rect_p1 = Point2D(0, 3)
    rect_p2 = Point2D(10, 23)
    num_points = 100

    points = list(generate_random_points(rect_p1, rect_p2, num_points))

    negative_points = [p for p in points if line.is_positive(p)]
    positive_points = [p for p in points if line.is_negative(p)]

    plt.figure(figsize=(10, 8))

    x_line = np.linspace(0, 10, 50)
    y_line = line.get_y(x_line)
    plt.plot(x_line, y_line, color='blue', label='Line: 2x - y + 3 = 0')

    plt.scatter(
        [p.x for p in positive_points],
        [p.y for p in positive_points],
        color='green',
        label='Positive Half-Plane',
        s=50,
    )

    plt.scatter(
        [p.x for p in negative_points],
        [p.y for p in negative_points],
        color='red',
        label='Negative Half-Plane',
        s=50,
    )

    plt.title('Points in Two Half-Planes')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()
