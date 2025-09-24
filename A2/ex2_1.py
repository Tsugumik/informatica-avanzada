import numpy as np


class Mean:
    def __init__(self):
        self.current_mean = 0.0
        self.count = 0

    def new(self, new_value):
        self.count += 1
        self.current_mean = self.current_mean + (new_value - self.current_mean) / self.count
        print(f"Current average: {self.current_mean}")

    def value(self):
        return self.current_mean


v = np.array([2, 7, 7, 18])
m = Mean()

for x in v:
    m.new(x)

print(f"Final average: {m.value()}")
print(f"NumPy mean: {np.mean(v)}")
