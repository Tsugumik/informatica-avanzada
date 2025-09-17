import math

num_terms_str = input("Enter the number of terms for the series: ")

n = int(num_terms_str)

# Method 1: Using a for loop
series_sum_loop = 0
for i in range(1, n + 1):
    series_sum_loop += 1 / (i ** 2)

pi_approx_loop = math.sqrt(6 * series_sum_loop)

# Method 2: Using a list comprehension and sum()
series_sum_lc = sum([1 / (i ** 2) for i in range(1, n + 1)])
pi_approx_lc = math.sqrt(6 * series_sum_lc)

pi_actual = math.pi

print(f"\nPi approximation (loop) with {n} terms: {pi_approx_loop}")
print(f"Pi approximation (list comprehension) with {n} terms: {pi_approx_lc}")
print(f"Actual value of Pi: {pi_actual}")

difference = abs(pi_actual - pi_approx_lc)
print(f"Difference: {difference}")



