# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return round(x / y, 2)

def modulus(x, y):
    if y == 0:
        return None
    return x % y

def exponent(x, y):
    return x ** y

def format_number(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return int(val)
    return val

def main():
    while True:
        print("\n============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")
        
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == "7":
            print("Goodbye!")
            break
            
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Invalid choice. Please select 1-7.")
            continue
            
        try:
            num1_input = input("Enter first number : ")
            num1 = float(num1_input)
            if num1 == int(num1):
                num1 = int(num1)
                
            num2_input = input("Enter second number: ")
            num2 = float(num2_input)
            if num2 == int(num2):
                num2 = int(num2)
        except ValueError:
            print("Error: Please enter valid numerical values.")
            continue
            
        if choice == "1":
            res = add(num1, num2)
            print(f"Result: {format_number(num1)} + {format_number(num2)} = {format_number(res)}")
        elif choice == "2":
            res = subtract(num1, num2)
            print(f"Result: {format_number(num1)} - {format_number(num2)} = {format_number(res)}")
        elif choice == "3":
            res = multiply(num1, num2)
            print(f"Result: {format_number(num1)} * {format_number(num2)} = {format_number(res)}")
        elif choice == "4":
            res = divide(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                formatted_res = f"{res:.2f}" if isinstance(res, float) and not res.is_integer() else str(res)
                if formatted_res.endswith(".0"):
                    formatted_res = formatted_res[:-2]
                print(f"Result: {format_number(num1)} / {format_number(num2)} = {formatted_res}")
        elif choice == "5":
            res = modulus(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {format_number(num1)} % {format_number(num2)} = {format_number(res)}")
        elif choice == "6":
            res = exponent(num1, num2)
            print(f"Result: {format_number(num1)} ** {format_number(num2)} = {format_number(res)}")

if __name__ == "__main__":
    main()
