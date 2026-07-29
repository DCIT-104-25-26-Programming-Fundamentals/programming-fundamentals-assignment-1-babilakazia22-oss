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

def calc_sum(numbers):
    """Return the sum of all numbers in the list using a loop."""
    total = 0
    for value in numbers:
        total += value
    return total


def calc_average(numbers):
    """Return the average of the numbers in the list."""
    # Avoid division by zero just in case
    if len(numbers) == 0:
        return 0
    total = calc_sum(numbers)
    return total / len(numbers)


def calc_max(numbers):
    """Return the maximum value in the list using a loop."""
    # Assume list is non-empty as per assignment input
    maximum = numbers[0]
    for value in numbers:
        if value > maximum:
            maximum = value
    return maximum


def calc_min(numbers):
    """Return the minimum value in the list using a loop."""
    # Assume list is non-empty as per assignment input
    minimum = numbers[0]
    for value in numbers:
        if value < minimum:
            minimum = value
    return minimum


def main():
    # Ask how many numbers
    n_input = input("How many numbers? ")
    n = int(n_input)

    # Validate N is positive
    if n <= 0:
        print("Error: Number of elements must be a positive integer.")
        return  # Stop the program

    numbers = []

    # Read n numbers from the user
    for i in range(1, n + 1):
        value_input = input(f"Enter number {i}: ")
        value = float(value_input)  # or int(...) if you only want integers
        numbers.append(value)

    # Compute statistics using functions
    total = calc_sum(numbers)
    average = calc_average(numbers)
    maximum = calc_max(numbers)
    minimum = calc_min(numbers)

    # Display results
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()