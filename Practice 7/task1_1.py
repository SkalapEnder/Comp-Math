import numpy as np
import math

def forward_difference_table(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    return table

def newton_forward_interpolation(x, y, x_interp):
    h = x[1] - x[0]  # Assuming equally spaced intervals
    s = (x_interp - x[0]) / h
    table = forward_difference_table(x, y)

    interp_value = table[0, 0]
    for i in range(1, len(x)):
        interp_value += (s * (s - 1) * ... * (s - i + 1) / np.math.factorial(i)) * table[0, i]

    return interp_value

def differentiate_newton_forward(x, y):
    h = x[1] - x[0]  # Assuming equally spaced intervals
    table = forward_difference_table(x, y)

    def derivative(x_val):
        s = (x_val - x[0]) / h
        deriv = 0
        for i in range(1, len(x)):
            factor = 1
            for j in range(1, i):
                factor *= (s - j)
            deriv += (factor / math.factorial(i-1)) * table[0, i]
        return deriv / h

    return derivative

# Given data
x_data = np.array([3, 5, 11, 27, 34])
y_data = np.array([-13, 23, 899, 17315, 35606])

# Get the derivative function
derivative_func = differentiate_newton_forward(x_data, y_data)

# Evaluate f'(10)
f_prime_10 = derivative_func(10)

print("Approximate f'(10):", f_prime_10)