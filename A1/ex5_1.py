def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]

    # Find the maximum of the rest of the list (all elements except the first).
    max_of_rest = find_max_recursive(lst[1:])

    # Compare the first element with the maximum of the rest of the list.
    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest


# --- Main program to test the function ---
my_list = [10, 5, 25, 8, 15]
maximum_value = find_max_recursive(my_list)
print(f"The maximum value in the list {my_list} is: {maximum_value}")