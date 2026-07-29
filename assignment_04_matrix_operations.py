# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    """Read a rows x cols matrix from the user."""
    matrix = []
    for i in range(1, rows + 1):
        row_str = input(f"Enter row {i}: ")
        # Split the line and convert each value to float or int
        values = row_str.split()
        if len(values) != cols:
            print("Error: You must enter exactly", cols, "values per row.")
            return None
        row = [float(v) for v in values]
        matrix.append(row)
    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    for row in matrix:
        # Print each value with some spacing
        line = ""
        for value in row:
            line += f"{value:8.2f}"
        print(line)


# PART A — Transpose a Matrix
def transpose_matrix(matrix):
    """Return the transpose of the given matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create result matrix with swapped dimensions (cols x rows)
    result = []
    for i in range(cols):
        result.append([0] * rows)

    # Fill result[j][i] = matrix[i][j]
    for i in range(rows):          # iterate over original rows
        for j in range(cols):      # iterate over original columns
            result[j][i] = matrix[i][j]
    return result


# PART B — Add Two Matrices
def add_matrices(A, B):
    """Return element-wise sum of matrices A and B using nested loops."""
    rows = len(A)
    cols = len(A[0])

    # Assume A and B have the same size (validated before calling)
    result = []
    for i in range(rows):
        result.append([0] * cols)

    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result


# PART C — Multiply Two Matrices
def multiply_matrices(A, B):
    """
    Return the product A x B using nested loops.
    A is M x N, B is N x P, result is M x P.
    """
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check that inner dimensions match (N in A == rows of B)
    if cols_A != rows_B:
        print("Error: Number of columns in A must equal number of rows in B.")
        return None

    # Initialize result matrix with zeros (M x P)
    result = []
    for i in range(rows_A):
        result.append([0] * cols_B)

    # Triple nested loop: i over rows of A, j over cols of B, k over common dimension
    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):   # or rows_B, same value
                total += A[i][k] * B[k][j]
            result[i][j] = total

    return result


def main():
    # -------------------------------
    # PART A — Transpose a Matrix
    # -------------------------------
    print("=== PART A: Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    matrix_A = read_matrix(m, n)
    if matrix_A is None:
        return

    print_matrix(matrix_A, "Original Matrix")
    transposed_A = transpose_matrix(matrix_A)
    print_matrix(transposed_A, "Transposed Matrix")

    # -------------------------------
    # PART B — Add Two Matrices
    # -------------------------------
    print("\n=== PART B: Add Two Matrices ===")
    m = int(input("Enter number of rows for matrices A and B: "))
    n = int(input("Enter number of columns for matrices A and B: "))

    print("Enter Matrix A:")
    matrix_B1 = read_matrix(m, n)
    if matrix_B1 is None:
        return

    print("Enter Matrix B:")
    matrix_B2 = read_matrix(m, n)
    if matrix_B2 is None:
        return

    sum_B = add_matrices(matrix_B1, matrix_B2)
    print_matrix(matrix_B1, "Matrix A")
    print_matrix(matrix_B2, "Matrix B")
    print_matrix(sum_B, "A + B")

    # -------------------------------
    # PART C — Multiply Two Matrices
    # -------------------------------
    print("\n=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter number of rows for Matrix A: "))
    n = int(input("Enter number of columns for Matrix A: "))
    p = int(input("Enter number of columns for Matrix B: "))

    print("Enter Matrix A:")
    matrix_C1 = read_matrix(m, n)
    if matrix_C1 is None:
        return

    print("Enter Matrix B:")
    # Matrix B must be N x P (rows = n)
    matrix_C2 = read_matrix(n, p)
    if matrix_C2 is None:
        return

    product_C = multiply_matrices(matrix_C1, matrix_C2)
    if product_C is None:
        return

    print_matrix(matrix_C1, "Matrix A")
    print_matrix(matrix_C2, "Matrix B")
    print_matrix(product_C, "A x B")


if __name__ == "__main__":
    main()