from Determinant import det

# Roots part
def characteristic_polynomial(matrix):
    # Convert to (A - λI)
    def subtract_lambda(matrix, lam):
        # Subtract lambda from the diagonal of the matrix
        return [[matrix[i][j] - lam if i == j else matrix[i][j] for j in range(len(matrix))]
                for i in range(len(matrix))]

    # Build polynomial as a function
    def poly(lam):
        mod_matrix = subtract_lambda(matrix, lam)
        return det(mod_matrix)

    return poly

def newton_raphson(poly, x0, poly_derivative, tol=1e-6, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        f = poly(x)
        df = poly_derivative(x)

        if abs(df) < tol:
            raise ValueError("Derivative too small, Newton-Raphson fails.")

        x_new = x - f / df

        if abs(x_new - x) < tol:
            return x_new
        x = x_new

    raise ValueError("Newton-Raphson method did not converge.")

# Vectors part
def gaussian_elimination(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(min(n, m)):
        # Find pivot row
        pivot = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                pivot = j

        # Swap rows
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]

        # Skip if pivot is zero
        if abs(matrix[i][i]) < 1e-9:
            continue

        # Normalize the pivot row
        pivot_value = matrix[i][i]
        for j in range(m):
            matrix[i][j] /= pivot_value

        # Eliminate below
        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(m):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix

def back_substitution(matrix):
    n = len(matrix)
    null_space = []
    free_vars = []

    # Identify pivot columns
    pivot_columns = [-1] * n
    for i in range(n):
        for j in range(n):
            if abs(matrix[i][j]) > 1e-9:
                pivot_columns[i] = j
                break
    
    # This comprampers all columns wit pivots to find free vars
    free_vars = [j for j in range(n) if j not in pivot_columns]

    for free_var in free_vars:
        vec = [0] * (n)
        vec[free_var] = 1
        for i in range(n - 1, -1, -1):
            if pivot_columns[i] != -1:
                vec[pivot_columns[i]] = -sum(matrix[i][j] * vec[j] for j in range(pivot_columns[i] + 1, n))
        null_space.append(vec)

    return null_space

# Enter functions
def find_vectors(matrix, eigenvalues):
    n = len(matrix)
    eigenvectors = {}

    for lam in eigenvalues:
        # Construct (A - λI)
        mod_matrix = [[matrix[i][j] - (lam if i == j else 0) for j in range(n)] for i in range(n)]

        # Append zero column (A | 0)
        augmented_matrix = [row + [0] for row in mod_matrix]

        reduced_matrix = gaussian_elimination(augmented_matrix)

        # Calculate vector for each values
        eigenvector = back_substitution(reduced_matrix)
        eigenvectors[lam] = eigenvector

    return eigenvectors

def find_roots(matrix):
    # Build polynomial
    poly = characteristic_polynomial(matrix)

    # Numerical approximation to find the derivative
    def derivative(x):
        h = 1e-6
        return (poly(x + h) - poly(x - h)) / (2 * h)

    # Initial guesses for roots (assume evenly spaced guesses)
    guesses = [i for i in range(-len(matrix), len(matrix) + 1)]
    roots = []

    for guess in guesses:
        try:
            root = newton_raphson(poly, guess, derivative)
            # Avoid duplicate roots (in float terms)
            if not any(abs(root - r) < 1e-5 for r in roots):
                roots.append(root)
        except ValueError:
            pass

    return roots

A = [[2., -1., 0],
     [-1., 2., -1.],
     [0, -1., 2.]
]

roots = find_roots(A)
vectors = find_vectors(A, roots)
print("Eigenvalues:", roots)
print("Eigenvectors:", vectors)