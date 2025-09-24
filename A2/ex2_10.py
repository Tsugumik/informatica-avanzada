from ex2_2 import Point2D
from ex2_9 import is_linearly_separable
from ex2_6 import random_line
import numpy as np
import matplotlib.pyplot as plt

def find_separating_line(set1, set2):
    all_points = set1 + set2
    if not all_points:
        return None

    all_x = [p.x for p in all_points]
    all_y = [p.y for p in all_points]

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    padding = 0.5
    bound_p1 = Point2D(min_x - padding, min_y - padding)
    bound_p2 = Point2D(max_x + padding, max_y + padding)

    iterations = 0
    max_iterations = 10000

    while iterations < max_iterations:
        try:
            line = random_line(bound_p1, bound_p2)
            if is_linearly_separable(line, set1, set2):
                print(f"Found a separating line after {iterations + 1} iterations.")
                return line
        except ValueError:
            # Skip vertical lines
            pass
        iterations += 1

    print("Could not find a separating line within the iteration limit.")
    return None

if __name__ == "__main__":
    iris = np.loadtxt('training.txt')

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

    separating_line = find_separating_line(setosa_points, non_setosa_points)

    if separating_line:
        plt.figure(figsize=(10, 8))

        plt.scatter([p.x for p in setosa_points], [p.y for p in setosa_points], color='blue', label='Setosa', s=50)
        plt.scatter([p.x for p in non_setosa_points], [p.y for p in non_setosa_points], color='green',
                    label='Versicolor/Virginica', s=50)

        x_vals = np.linspace(min([p.x for p in setosa_points + non_setosa_points]) - 1,
                             max([p.x for p in setosa_points + non_setosa_points]) + 1,
                             100)
        y_vals = separating_line.get_y(x_vals)
        plt.plot(x_vals, y_vals, color='red', linestyle='--', label='Separating Line')

        plt.title('Randomly Found Separating Line for Iris Setosa')
        plt.xlabel('Petal Length (cm)')
        plt.ylabel('Petal Width (cm)')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Failed to find and plot a separating line.")
