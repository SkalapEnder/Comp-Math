from Determinant import det

def cramer(A, b):
    # Edge case
    if det(A) == 0: 
        return None

    n = len(b)
    solution = [0] * n

    for i in range(n):
        D = [row[:] for row in A]
        for j in range(n):
            D[j][i] = b[j]

        solution[i] = det(D) / det(A)

    return solution

A = [[20., 1., -2.],
     [3., 20., -1.],
     [2., -3., 20.]
]
b = [17., -18., 25.]

solution = cramer(A, b)
if solution is not None:
    print("Solution:", [round(val, 4) for val in solution])
else:
    print("Determinant of matrix is zero")