def apply(iterable1, iterable2, f=None):
    if f is None:
        def add(x, y):
            return x + y

        f = add

    for item1, item2 in zip(iterable1, iterable2):
        yield f(item1, item2)

# Example 1: With the default operation (addition)
list1 = [3, 4, 5]
list2 = [1, 4, -1]
result_add = list(apply(list1, list2))
print(result_add)

# Example 2: With a custom operation (multiplication)
result_multiply = list(apply(range(3, 6), [1, 4, -1], lambda x, y: x * y))
print(result_multiply)