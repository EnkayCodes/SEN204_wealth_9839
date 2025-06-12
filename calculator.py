def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return
    
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
