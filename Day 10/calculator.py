# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     return n1 * n2
#
# def div(n1, n2):
#     return n1 / n2
#
# calc_dict = {
#     "+": add,
#     "-": sub,
#     "*": mul,
#     "/": div
# }
#
# result = calc_dict["*"](4,6)
# print(result)
#
# def calculator():
#     print("Welcome to the Python Calculator!")
#     while True:
#         num1 = float(input("What is the first number?: "))
#         operator = input("Pick an operation: +, -, *, /")
#         num2 = float(input("What is the next number?: "))
#         calc_function = calc_dict[operator]
#         answer = calc_function(num1, num2)
#         print(f"{num1} {operator} {num2} = {answer}")

def calculator():
    """
    A calculator that performs basic operations and allows the user to either
    work with the previous result or start a new calculation.
    """
    calc_dict = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }

    # Initialize "previous_result" as None to track calculations
    previous_result = None

    while True:
        # Check if a previous result exists
        if previous_result is not None:
            user_choice = input("Do you want to use the previous result? (yes/no): ").strip().lower()
            if user_choice == "yes":
                first_number = previous_result
            else:
                previous_result = None  # Explicitly reset, even though it's unnecessary here
                first_number = float(input("Enter the first number: "))
        else:
            first_number = float(input("Enter the first number: "))

        # Ask for the operator
        operator = input("Enter an operator (+, -, *, /): ").strip()
        while operator not in calc_dict:
            operator = input("Invalid operator. Enter one of (+, -, *, /): ").strip()

        # Ask for the second number
        second_number = float(input("Enter the second number: "))

        # Perform the calculation
        operation = calc_dict[operator]
        result = operation(first_number, second_number)

        print(f"The result of {first_number} {operator} {second_number} is: {result}")

        # Store the result for the next loop
        if isinstance(result, (int, float)):
            previous_result = result
        else:
            # If there's an error (like division by zero), ignore the result
            previous_result = None

        # Ask the user if they want to continue
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator
calculator()
