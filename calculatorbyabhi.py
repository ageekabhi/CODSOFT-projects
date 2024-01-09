import math

def basic_calculator():
    print("Basic Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operator")
            return

        print("Result:", result)
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def scientific_calculator():
    print("Scientific Calculator")
    print("Functions: sin, cos, tan, sqrt, log, exp")
    
    try:
        function = input("Enter the function: ").lower()

        if function in ["sin", "cos", "tan"]:
            angle = float(input("Enter the angle in degrees: "))
            angle_rad = math.radians(angle)
            if function == "sin":
                result = math.sin(angle_rad)
            elif function == "cos":
                result = math.cos(angle_rad)
            elif function == "tan":
                result = math.tan(angle_rad)
        elif function == "sqrt":
            num = float(input("Enter the number: "))
            result = math.sqrt(num)
        elif function == "log":
            num = float(input("Enter the number: "))
            result = math.log10(num)
        elif function == "exp":
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = math.pow(base, exponent)
        else:
            print("Invalid function")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def main():
    print("Simple Calculator")
    print("Options: 1 - Basic Calculator, 2 - Scientific Calculator, 3 - Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            basic_calculator()
        elif choice == "2":
            scientific_calculator()
        elif choice == "3":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()