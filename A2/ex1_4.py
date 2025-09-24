import numpy as np

def integrate_trapezoidal(a, b, N=1000):

    def p(t):
        return 1 / (1 + np.exp(-t))

    # Calculate the width of each subinterval
    delta_x = (b - a) / N

    x_values = np.linspace(a, b, N + 1)
    f_values = p(x_values)

    # Apply the trapezoidal rule formula
    internal_sum = np.sum(f_values[1:-1])

    # Calculate the full integral approximation
    integral_approx = (delta_x / 2) * (f_values[0] + 2 * internal_sum + f_values[-1])

    return integral_approx


# Test
a = -100
b = 100
approx_val = integrate_trapezoidal(a, b)
print(approx_val)

# Fewer subintervals
a_1 = 0
b_1 = 5
n = 100
approx_val_1 = integrate_trapezoidal(a_1, b_1, n)
print(approx_val_1)

