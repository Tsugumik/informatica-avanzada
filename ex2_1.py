number1 = float(input("Number 1: "))
character = input("Character: ")
number2 = float(input("Number 2: "))

if character == '+':
    print(f"{number1} + {number2} = {number1 + number2}")
elif character == '-':
    print(f"{number1} - {number2} = {number1 - number2}")
elif character == '*' or character == 'x':
    print(f"{number1} * {number2} = {number1 * number2}")
elif character == '/':
    print(f"{number1} / {number2} = {number1 / number2}")
else:
    print("Operation not implemented")