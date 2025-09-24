operation_str = input("Enter a simple math operation (e.g.7*1.5): ")

operator = ""
index_of_operator = -1

if "+" in operation_str:
    operator = "+"
    index_of_operator = operation_str.find("+")
elif "-" in operation_str:
    operator = "-"
    index_of_operator = operation_str.find("-")
elif "*" in operation_str:
    operator = "*"
    index_of_operator = operation_str.find("*")
elif "x" in operation_str:
    operator = "*"
    index_of_operator = operation_str.find("x")
elif "/" in operation_str:
    operator = "/"
    index_of_operator = operation_str.find("/")

if operator != "":
    num1_str = operation_str[:index_of_operator]
    num2_str = operation_str[index_of_operator + 1:]

    operand1 = float(num1_str)
    operand2 = float(num2_str)

    result = None

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            result = operand1 / operand2
        else:
            print("Error: Division by zero.")
            exit()

    print(f"Result: {result}")

else:
    print("Error: No valid operator found.")