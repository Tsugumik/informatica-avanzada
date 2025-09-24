import numpy as np

def all_rows_are_same(matrix):
    np_matrix = np.array(matrix)

    # Check if the matrix is empty or has only one row.
    # If so, they are considered the same.
    if np_matrix.shape[0] < 2:
        return True

    first_row = np_matrix[0, :]

    # Compare all rows to the first row. The all() function
    # returns True only if all elements in the comparison are True.
    return np.all(np_matrix == first_row)

matrix1 = [[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]]

matrix2 = [[1, 2, 3],
           [1, 2, 4],
           [1, 2, 3]]

print(f"Are all rows in matrix1 the same? {all_rows_are_same(matrix1)}")
print(f"Are all rows in matrix2 the same? {all_rows_are_same(matrix2)}")
