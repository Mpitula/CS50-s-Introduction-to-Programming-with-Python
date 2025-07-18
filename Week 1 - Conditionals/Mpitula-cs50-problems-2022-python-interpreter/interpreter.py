expression = input("Expression: ").strip()

expression = expression.split(" ")

x = float(expression[0])
z = expression[1]
y = float(expression[2])

match z:
    case "+":
        result = x + y

    case "-":
        result = x - y
    case "*":
        result = x * y
    case "/":
        result = x / y
print(round(result, 1))

