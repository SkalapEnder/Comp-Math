def jacobi_iteration(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0[:]

    for iteration in range(max_iterations):
        x_new = x[:]

        for i in range(n):
            sum_terms_1 = sum(A[i][j] * x[j] for j in range(n) if j != i)

            x_new[i] = (b[i] - sum_terms_1) / A[i][i]
        # Error tolerance
        if max([abs(x_new[i] - x[i]) for i in range(n)]) < tol:
            return x_new

        x = x_new

    return x


A = [[20., 1., -2.],
     [3., 20., -1.],
     [2., -3., 20.]
]
b = [17., -18., 25.]
x0 = [0, 0, 0]

solution = jacobi_iteration(A, b, x0)
if solution is not None:
    print("Solution:", [round(val, 4) for val in solution])
else:
    print("Convergence not reached.")