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

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = matrix[r][c]
    return transposed

def add_matrices(matrixA, matrixB):
    rowsA, colsA = len(matrixA), len(matrixA[0])
    rowsB, colsB = len(matrixB), len(matrixB[0])
    if rowsA != rowsB or colsA != colsB:
        return None
    
    result = [[0] * colsA for _ in range(rowsA)]
    for r in range(rowsA):
        for c in range(colsA):
            result[r][c] = matrixA[r][c] + matrixB[r][c]
    return result

def multiply_matrices(matrixA, matrixB):
    rowsA, colsA = len(matrixA), len(matrixA[0])
    rowsB, colsB = len(matrixB), len(matrixB[0])
    if colsA != rowsB:
        return None
    
    result = [[0] * colsB for _ in range(rowsA)]
    for r in range(rowsA):
        for c in range(colsB):
            for k in range(colsA):
                result[r][c] += matrixA[r][k] * matrixB[k][c]
    return result

def print_matrix(matrix):
    if not matrix:
        return
    str_matrix = [[str(elem) for elem in row] for row in matrix]
    col_widths = [max(len(row[col]) for row in str_matrix) for col in range(len(matrix[0]))]
    for row in str_matrix:
        formatted_row = "  ".join(elem.rjust(col_widths[i]) for i, elem in enumerate(row))
        print(formatted_row)

def read_matrix(name="Matrix"):
    while True:
        try:
            rows = int(input(f"Enter number of rows for {name}: "))
            cols = int(input(f"Enter number of columns for {name}: "))
            if rows <= 0 or cols <= 0:
                print("Dimensions must be positive integers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter integers.")
            
    matrix = []
    for i in range(1, rows + 1):
        while True:
            row_input = input(f"Enter row {i}: ")
            parts = row_input.split()
            if len(parts) != cols:
                print(f"Error: You must enter exactly {cols} values.")
                continue
            try:
                row_values = []
                for val in parts:
                    if '.' in val:
                        num = float(val)
                        if num == int(num):
                            num = int(num)
                    else:
                        num = int(val)
                    row_values.append(num)
                matrix.append(row_values)
                break
            except ValueError:
                print("Error: Invalid numbers. Please enter numerical values.")
    return matrix

def main():
    while True:
        print("\n============================")
        print("   MATRIX OPERATIONS MENU")
        print("============================")
        print("1. Transpose a Matrix (Part A)")
        print("2. Add Two Matrices (Part B)")
        print("3. Multiply Two Matrices (Part C)")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n--- Part A: Transpose a Matrix ---")
            mat = read_matrix("Matrix")
            print("\nOriginal Matrix:")
            print_matrix(mat)
            trans = transpose_matrix(mat)
            print("\nTransposed Matrix:")
            print_matrix(trans)
            
        elif choice == "2":
            print("\n--- Part B: Add Two Matrices ---")
            print("Enter details for Matrix A:")
            matA = read_matrix("Matrix A")
            print("Enter details for Matrix B:")
            matB = read_matrix("Matrix B")
            
            print("\nMatrix A:")
            print_matrix(matA)
            print("\nMatrix B:")
            print_matrix(matB)
            
            sum_mat = add_matrices(matA, matB)
            if sum_mat is None:
                print("\nError: Matrices must have the same dimensions for addition.")
            else:
                print("\nSum Matrix:")
                print_matrix(sum_mat)
                
        elif choice == "3":
            print("\n--- Part C: Multiply Two Matrices ---")
            print("Enter details for Matrix A:")
            matA = read_matrix("Matrix A")
            print("Enter details for Matrix B:")
            matB = read_matrix("Matrix B")
            
            print("\nMatrix A:")
            print_matrix(matA)
            print("\nMatrix B:")
            print_matrix(matB)
            
            prod_mat = multiply_matrices(matA, matB)
            if prod_mat is None:
                print("\nError: Multiplication not possible. Columns in A must equal rows in B.")
            else:
                print("\nProduct Matrix:")
                print_matrix(prod_mat)
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
