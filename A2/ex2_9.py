from ex2_2 import Point2D
from ex2_4 import LinearEquation
import numpy as np
import matplotlib.pyplot as plt


def is_linearly_separable(line, set1, set2):
    if not set1 or not set2:
        return True

    first_point_eval = line.evaluate(set1[0])

    if first_point_eval == 0:
        return False

    for p in set1:
        if (line.evaluate(p) * first_point_eval) <= 0:
            return False

    for p in set2:
        if (line.evaluate(p) * first_point_eval) >= 0:
            return False

    return True

if __name__ == "__main__":
    iris = np.loadtxt("training.txt")

    petal_length = iris[:, 2]
    petal_width = iris[:, 3]
    species = iris[:, 4]

    setosa_points = []
    non_setosa_points = []

    for i in range(len(species)):
        p = Point2D(petal_length[i], petal_width[i])
        if species[i] == 1:
            setosa_points.append(p)
        else:
            non_setosa_points.append(p)

    line1 = LinearEquation(a=0.56, b=2.2, c=-3.5)
    is_separable1 = is_linearly_separable(line1, setosa_points, non_setosa_points)

    line2 = LinearEquation(a=-0.8, b=4.3, c=-3.5)
    is_separable2 = is_linearly_separable(line2, setosa_points, non_setosa_points)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    ax1.set_title(f'Line 1: 0.56x + 2.2y - 3.5 = 0\nSeparates Sets: {is_separable1}')
    ax1.scatter([p.x for p in setosa_points], [p.y for p in setosa_points], color='blue', label='Setosa', s=50)
    ax1.scatter([p.x for p in non_setosa_points], [p.y for p in non_setosa_points], color='green',
                label='Versicolor/Virginica', s=50)
    x_vals = np.linspace(0, 7, 100)
    y_vals1 = line1.get_y(x_vals)
    ax1.plot(x_vals, y_vals1, color='red', linestyle='--', label='Line')
    ax1.set_xlabel('Petal Length (cm)')
    ax1.set_ylabel('Petal Width (cm)')
    ax1.legend()
    ax1.grid(True)

    ax2.set_title(f'Line 2: -0.8x + 4.3y - 3.5 = 0\nSeparates Sets: {is_separable2}')
    ax2.scatter([p.x for p in setosa_points], [p.y for p in setosa_points], color='blue', label='Setosa', s=50)
    ax2.scatter([p.x for p in non_setosa_points], [p.y for p in non_setosa_points], color='green',
                label='Versicolor/Virginica', s=50)
    y_vals2 = line2.get_y(x_vals)
    ax2.plot(x_vals, y_vals2, color='red', linestyle='--', label='Line')
    ax2.set_xlabel('Petal Length (cm)')
    ax2.set_ylabel('Petal Width (cm)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()