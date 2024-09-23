def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Display the menu to the user
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for the operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the user input is valid
    if choice in ['1', '2', '3', '4']:
        # Get numbers from the user
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # Perform the corresponding operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")


calculator()