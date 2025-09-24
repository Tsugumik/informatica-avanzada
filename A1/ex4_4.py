import random


def random_sample(items, k):
    n = len(items)
    if k > n or k < 0:
        return []

    sample = []
    chosen_count = 0

    for j in range(n):
        p = (k - chosen_count) / (n - j)

        if random.random() <= p:
            sample.append(items[j])
            chosen_count += 1

        if chosen_count == k:
            break

    return sample


# A list of items to draw from
my_list = ['a', 'b', 'c', 'd', 'e']

# The size of the sample
k_items = 3

# The number of simulations to run for all unique combinations
# (not each)
num_simulations = 1000000

# A dictionary to count the occurrences of each sample combination
occurrences = {}

# Run the simulation
for _ in range(num_simulations):
    # Generate a sample
    sample = random_sample(my_list, k_items)

    # Convert the list to a tuple to use it as a dictionary key
    sample_tuple = tuple(sorted(sample))

    # Count the occurrence of this tuple
    if sample_tuple in occurrences:
        occurrences[sample_tuple] += 1
    else:
        occurrences[sample_tuple] = 1

# Display the results
print(f"Simulation of {num_simulations} samples of size {k_items} from {my_list}")
print("Occurrences of each unique combination:")

for combo, count in occurrences.items():
    print(f"{combo} --> {count}")