import numpy as np
import matplotlib.pyplot as plt

iris = np.loadtxt('training.txt')

petal_length = iris[:, 2]
petal_width = iris[:, 3]

species = iris[:, 4]

plt.figure(figsize=(10, 8))

colors = {1: 'blue', 2: 'green', 3: 'red'}
labels = {1: 'setosa', 2: 'versicolor', 3: 'virginica'}

for s in np.unique(species):
    indices = species == s

    plt.scatter(
        petal_length[indices],
        petal_width[indices],
        color=colors[s],
        label=labels[s],
        alpha=0.7,
        edgecolors='k',
        s=80
    )

plt.title('Iris Plants: Petal Length vs. Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend()
plt.grid(True)
plt.show()