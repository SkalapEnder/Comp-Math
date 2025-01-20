def gauss_elimination(A, B):
    n = len(B)
    for i in range(n):
        # Make the pivot point
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        B[i] /= pivot

        # Forward elimination
        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    return x