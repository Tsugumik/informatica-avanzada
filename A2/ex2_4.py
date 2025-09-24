import numpy as np
import matplotlib.pyplot as plt


class LinearEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_y(self, x):
        if self.b == 0:
            raise ValueError("Cannot calculate y for a vertical line (b=0)")

        return (-self.a * x - self.c) / self.b

    def evaluate(self, p):
        return self.a * p.x + self.b * p.y + self.c

    def is_positive(self, p):
        return self.evaluate(p) > 0

    def is_negative(self, p):
        return self.evaluate(p) < 0

if __name__ == "__main__":
    line = LinearEquation(a=2, b=-1, c=3)

    x_start = 0
    x_end = 10
    num_points = 500

    x_values = np.linspace(x_start, x_end, num_points)

    y_values = line.get_y(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label='2x - y + 3 = 0')
    plt.title('Plot of the Line 2x - y + 3 = 0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()
