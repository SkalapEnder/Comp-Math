import numpy as np

def jacobi_iteration(A, b, x0, tol=1e-6, max_iter=1000):
    """
    Performs Jacobi iteration to solve the linear system Ax = b.

    Args:
        A: Coefficient matrix (numpy array)
        b: Constant vector (numpy array)
        x0: Initial guess for the solution vector (numpy array)
        tol: Tolerance for convergence
        max_iter: Maximum number of iterations

    Returns:
        Solution vector (numpy array) or None if convergence is not reached
    """

    n = len(b)
    x = x0.copy()

    for _ in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new

    return None  # Convergence not reached

# Example usage
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])
b = np.array([6., 25., -11., 15.])
x0 = np.zeros_like(b)  # Initial guess

solution = jacobi_iteration(A, b, x0)

if solution is not None:
    print("Solution:", solution)
else:
    print("Convergence not reached.")