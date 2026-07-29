# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# PART A — Single Table
def print_single_table(number):
    """
    Print the multiplication table for 'number' from 1 to 12.
    """
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):  # 1 to 12
        result = number * i
        print(f"{number} x {i} = {result}")


# PART B — Bonus: Tables from 1 to N
def print_tables_1_to_N(N):
    """
    Print full multiplication tables from 1 to N (each from 1 to 12),
    with a separator line between tables.
    """
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    for num in range(1, N + 1):
        print_single_table(num)
        print("---------------------------")  # separator between tables


def main():
    # -------------------------------
    # PART A — Single Table
    # -------------------------------
    num_input = input("Enter a number for a single table: ")
    num = int(num_input)

    print_single_table(num)

    # -------------------------------
    # PART B — Tables from 1 to N
    # -------------------------------
    N_input = input("Enter N (for tables from 1 to N): ")
    N = int(N_input)

    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    print_tables_1_to_N(N)


if __name__ == "__main__":
    main()