from Determinant import det

def inverse_matrix(matrix):
  n = len(matrix)

  # Create an second (I) matrix (1s on diagonal)
  inverse = [[float(i == j) for i in range(n)] for j in range(n)]

  for i in range(n):
    pivot = i

    for j in range(i + 1, n):
      if abs(matrix[j][i]) > abs(matrix[pivot][i]):
        pivot = j

    matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
    inverse[i], inverse[pivot] = inverse[pivot], inverse[i]

    if matrix[i][i] == 0:
      return None  # Matrix's det is 0 --> Matrix is not invertible

    # Elimination left matrix row to pivot row
    factor = 1 / matrix[i][i]
    for j in range(n):
      matrix[i][j] *= factor
      inverse[i][j] *= factor

    # Elimination down in each column
    for j in range(n):
      if j == i: # Pass diagonals
        continue

      factor = matrix[j][i]
      for k in range(n):
        matrix[j][k] -= factor * matrix[i][k]
        inverse[j][k] -= factor * inverse[i][k]

  return inverse

def print_matrix(matrix):
    for i in range(len(matrix)):
        row = str(i) + ' |  '
        for j in range(len(matrix[0])):
            row += str(round(matrix[i][j], 6)) + '  |  '
        print(row)

A = [[20., 1., -2.],
     [3., 20., -1.],
     [2., -3., 20.]
]

In = inverse_matrix(A)
if In != None:
    print("\tInverse matrix:")
    print_matrix(In)
else:
    print("There is no inverse for this matrix!")