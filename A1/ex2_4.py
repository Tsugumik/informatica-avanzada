n_str = input("Enter a non-negative number (n) for the triangle's size: ")
n = int(n_str)

if n < 0:
    print("Please enter a non-negative number.")
else:
    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end="")
        print()