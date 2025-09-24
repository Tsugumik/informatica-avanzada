def add_list_items(my_list):
    total = 0
    try:
        for item in my_list:
            total += item
        return total
    except TypeError:
        raise TypeError("Incompatible data types")

# Example 1: A list with compatible data types (numbers)
list1 = [10, 20, 30, 40]
try:
    sum1 = add_list_items(list1)
    print(f"The sum of the list {list1} is: {sum1}")
except TypeError as e:
    print(e)

print("-" * 20)

# Example 2: A list with incompatible data types (number and string)
list2 = [10, 20, "hello", 40]
try:
    sum2 = add_list_items(list2)
    print(f"The sum of the list {list2} is: {sum2}")
except TypeError as e:
    print(e)