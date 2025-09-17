def sum_iterables(iterable1, iterable2):
    for item1, item2 in zip(iterable1, iterable2):
        # yield returns one item at a time pausing the function execution
        yield item1 + item2

# Example 1: Summing two lists
list1 = [3, 4, 5]
list2 = [1, 4, -1]
result_list = list(sum_iterables(list1, list2))
print(result_list)

# Example 2: Summing a range and a list
range_obj = range(1, 5)
list_obj = [10, 20, 30, 40]
result_range = list(sum_iterables(range_obj, list_obj))
print(result_range)