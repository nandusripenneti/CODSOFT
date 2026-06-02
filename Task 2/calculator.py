a = float(input("Enter first number: "))
ch = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))


if ch == "+":
    print("Result:", a + b)
elif ch == "-":
    print("Result:", a - b)
elif ch == "*":
    print("Result:", a * b)
elif ch == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator")
