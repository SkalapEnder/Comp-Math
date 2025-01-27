import numpy as np

def find_polynomial_coefficients(x_values, y_values):
    n = len(x_values)
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(n):
        for j in range(n):
            A[i, j] = x_values[i] ** j

        B[i] = y_values[i]

    coefficients = np.linalg.solve(A, B)
    return coefficients

def evaluate_polynomial(coefficients, x):
    y = 0
    for i in range(len(coefficients)):
        y += coefficients[i] * x ** i
    return y


x_values = [0, 1, 2, 3, 4]
y_values = [1, -1, 1, -1, 1]

coefficients = find_polynomial_coefficients(x_values, y_values)

for x in range(5, 7 + 1):
    y = evaluate_polynomial(coefficients, x)
    print(f"x = {x}, y = {y}")