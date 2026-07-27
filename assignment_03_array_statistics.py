# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0.0
    return calculate_sum(numbers) / len(numbers)

def calculate_max(numbers):
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum

def calculate_min(numbers):
    if len(numbers) == 0:
        return None
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum

def format_number(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return int(val)
    return val

def main():
    try:
        n_input = input("How many numbers? ")
        n = int(n_input)
        if n <= 0:
            print("Error: The number of elements must be a positive integer.")
            return
        
        numbers = []
        for i in range(1, n + 1):
            val_input = input(f"Enter number {i}: ")
            numbers.append(float(val_input))
        
        total_sum = calculate_sum(numbers)
        avg = calculate_average(numbers)
        maximum = calculate_max(numbers)
        minimum = calculate_min(numbers)
        
        print("\nResults:")
        print(f"Sum:     {format_number(total_sum)}")
        print(f"Average: {format_number(avg)}")
        print(f"Maximum: {format_number(maximum)}")
        print(f"Minimum: {format_number(minimum)}")
        
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
