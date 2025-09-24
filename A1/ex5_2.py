def gcd_iterative(a, b):
    # Ensure a is the larger number
    if b > a:
        a, b = b, a

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def gcd_recursive(a, b):
    # if b is 0, a is the GCD
    if b == 0:
        return a

    # call the function with the smaller number and the remainder
    return gcd_recursive(b, a % b)

num1 = 93164
num2 = 5826

result_iterative = gcd_iterative(num1, num2)
result_recursive = gcd_recursive(num1, num2)
print(f"The GCD of {num1} and {num2} using the recursive method is: {result_recursive}")
print(f"The GCD of {num1} and {num2} using the iterative method is: {result_iterative}")