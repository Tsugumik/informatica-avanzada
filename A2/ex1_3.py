from ex1_2 import estimate_pi
import numpy as np
import matplotlib.pyplot as plt

def generate_plot():
    sample_sizes = np.arange(5, 5005, 10)

    pi_estimates = []

    for size in sample_sizes:
        estimate = estimate_pi(size)
        pi_estimates.append(estimate)

    plt.figure(figsize=(10, 6))

    plt.plot(sample_sizes, pi_estimates, marker='o', linestyle='-', color='b',
             label='Estimated Pi')

    plt.axhline(y=np.pi, color='r', linestyle='-', label='Actual Pi')

    plt.title('Approximation of Pi as Sample Size Increases')
    plt.xlabel('Sample Size')
    plt.ylabel('Estimated Pi')
    plt.legend()
    plt.grid(True)
    plt.show()

generate_plot()