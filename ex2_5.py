import random

num_rolls = int(input("Enter the number of times to roll the die: "))

counts = [0, 0, 0, 0, 0, 0, 0]

for _ in range(num_rolls):
    roll = random.randint(1, 6)
    counts[roll] += 1

print("\n--- Simulation Results ---")
for i in range(1, 7):
    relative_frequency = counts[i] / num_rolls
    print(f"Number {i}: Occurrences = {counts[i]}, Relative Frequency = {relative_frequency:.4f}")