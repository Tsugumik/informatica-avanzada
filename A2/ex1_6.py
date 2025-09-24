import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

num_walks = 20
walk_length = 100

plt.figure(figsize=(10, 6))
for _ in range(num_walks):
    steps = np.random.randn(walk_length - 1)

    path = np.concatenate(([0], np.cumsum(steps)))

    plt.plot(path, alpha=0.7)

plt.title(f"{num_walks} Random Walks of Length {walk_length}")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()