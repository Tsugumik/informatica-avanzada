import numpy as np

def integral(f, a, b, N=1000):
    delta_x = (b - a) / N

    x_values = np.linspace(a, b, N + 1)
    f_values = f(x_values)

    internal_sum = np.sum(f_values[1:-1])

    integral_approx = (delta_x / 2) * (f_values[0] + 2 * internal_sum + f_values[-1])

    return integral_approx

def normal_distribution(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-(x**2 / 2))

result1 = integral(lambda x: 1 / (1 + np.exp(-x)), -100, 100)
print(result1)
result2 = integral(np.sin, 0, np.pi * 2)
print(result2)
result3 = integral(normal_distribution, -10, 10)
print(result3)

