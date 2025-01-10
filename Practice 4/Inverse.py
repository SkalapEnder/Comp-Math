from Determinant import det

def get_minor(matrix, row, col):
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

def adjugate_matrix(A):
    adj = []
    for r in range(len(A)):
        adj_row = []

        for c in range(len(A)):
            minor = get_minor(A, r, c)
            cofactor = ((-1) ** (r + c)) * det(minor)
            adj_row.append(cofactor)

        adj.append(adj_row)
    return transpose_matrix(adj)

def transpose_matrix(matrix):
    """Transpose a matrix."""
    return [list(row) for row in zip(*matrix)]

def invert_matrix(A):
    deter = det(A)
    if deter == 0:  
        return None
    adj = adjugate_matrix(A)
    return [[adj[r][c] / deter for c in range(len(adj))] for r in range(len(adj))]

def print_matrix(matrix):
    for row in matrix:
        t = '|  '
        for col in row:
            t += str(round(col, 8))
            t += '   '
        t += ' |'
        print(t)

A = [[20., 1., -2.],
     [3., 20., -1.],
     [2., -3., 20.]
]
In = invert_matrix(A)
if In != None:
    print("Inverse matrix")
    print_matrix(In)
else:
    print("There is no inverse for this matrix!")