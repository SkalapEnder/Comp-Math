def det(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return 0

    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


    # Recursive case for n>2 matrices
    det_result = 0
    for col in range(len(matrix)):
        # Create the minor matrix by excluding the current row and column
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]

        # Alternate signs for cofactors (-1)^(row+col)
        sign = (-1) ** col
        det_result += sign * matrix[0][col] * det(minor)

    return det_result