n_str = input("Enter a number (n) to find all primes up to it: ")
n = int(n_str)

if n < 2:
    print("There are no prime numbers less than 2.")
else:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    print(f"The prime numbers up to {n} are:")
    for i in range(2, n + 1):
        if is_prime[i]:
            print(i, end=" ")
    print()