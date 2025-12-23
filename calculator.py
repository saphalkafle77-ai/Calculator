# small calculator for basic operation
def calculator(operation):
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    if operation == "+":
        print(a + b)
    if operation == "-":
        print(a - b)
    if operation == "*":
        print(a * b)
    if operation == "/":
        print(a / b)


(calculator("+"))
