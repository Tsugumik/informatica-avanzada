from ex2_4 import LinearEquation
from ex2_2 import Point2D
import numpy as np
import matplotlib.pyplot as plt

def line_from_points(p1, p2):
    a = p2.y - p1.y
    b = -(p2.x - p1.x)
    c = -(p1.x * a + p1.y * b)

    return LinearEquation(a, b, c)

if __name__ == "__main__":
    point1 = Point2D(0, 3)
    point2 = Point2D(10, 23)

    line = line_from_points(point1, point2)

    print(f"The line passing through {point1} and {point2} has the equation:")
    print(f"a = {line.a}, b = {line.b}, c = {line.c}")
    print(f"Which represents the equation: {line.a}x + ({line.b})y + ({line.c}) = 0")

    x_values = np.linspace(0, 10, 500)
    y_values = line.get_y(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'{line.a}x + ({line.b})y + ({line.c}) = 0')
    plt.scatter(point1.x, point1.y, color='red', marker='o', s=100, label='Point 1')
    plt.scatter(point2.x, point2.y, color='green', marker='o', s=100, label='Point 2')

    plt.title('Line Passing Through Two Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()