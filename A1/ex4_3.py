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

# A sample list to draw from
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# The size of the sample to generate
k_items = 4

# Generate the random sample
my_sample = random_sample(my_list, k_items)

print(f"The original list: {my_list}")
print(f"A random sample of {k_items} items is: {my_sample}")