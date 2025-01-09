def gauss_elimination(matrix):
    n = len(matrix)

    # Forward elimination
    for i in range(n):
        # Find the pivot element
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))

        # Swap rows
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # i - max and pivot row
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            # Make all j (vertical values) to zero under k (column)
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Back substitution from end
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][-1] / matrix[i][i]
        # Move to upper row to eliminate numbers
        for j in range(i - 1, -1, -1):
            matrix[j][-1] -= matrix[j][i] * solution[i]

    print_vector("Solution:", solution)

def print_vector(label, vector):
    print(label)
    for i in range(len(vector)):
        print(round(vector[i], 2))

# Example usage
matrix = [
    [20, 1, -2, 17],
    [3, 20, -1, -18],
    [2, -3, 20, 25]
]

solution = gauss_elimination(matrix)



