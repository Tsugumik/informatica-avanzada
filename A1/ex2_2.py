vector_a_in = input("Enter 3 numbers: ").split()
vector_a = [float(x) for x in vector_a_in]

vector_b_in = input("Enter 3 numbers: ").split()
vector_b = [float(x) for x in vector_b_in]

dot_product = sum([a * b for a, b in zip(vector_a, vector_b)])

print(f"Dot product: {dot_product}")