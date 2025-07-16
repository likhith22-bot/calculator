def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! can't divide by zero."
    return a / b

def calculator():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(first_number, second_number))
        elif choice == '2':
            print("Result:", subtract(first_number, second_number))
        elif choice == '3':
            print("Result:", multiply(first_number, second_number))
        elif choice == '4':
            print("Result:", divide(first_number, second_number))
        else:
            print("Invalid choice. Please select from 1 to 5.")
calculator()
