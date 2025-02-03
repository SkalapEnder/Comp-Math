def forward_difference_table(x, y):
    n = len(x)
    table = [[0] * n for _ in range(n)]  # Create a 2D list for the table
    table[0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    return table

def newton_forward_derivative(x, y, x_interp, order):
    h = x[1] - x[0]  # Assuming equally spaced intervals
    table = forward_difference_table(x, y)
    s = (x_interp - x[0]) / h

    if order == 1:
        derivative = (table[0][1] - 0.5 * table[0][2] + (1/3) * table[0][3] - ...) / h
    elif order == 2:
        derivative = (table[0][2] - table[0][3] + (3/4) * table[0][4] - ...) / h**2
    elif order == 3:
        derivative = (table[0][3] - (3/2) * table[0][4] + (11/6) * table[0][5] - ...) / h**3
    else:
        raise ValueError("Invalid derivative order. Must be 1, 2, or 3.")

    return derivative

# Given data
x_data = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
y_data = [1.000, 1.025, 1.049, 1.072, 1.095, 1.118, 1.140]

# Calculate derivatives at x = 1.05
first_derivative_105 = newton_forward_derivative(x_data, y_data, 1.05, 1)
second_derivative_105 = newton_forward_derivative(x_data, y_data, 1.05, 2)

# Calculate derivatives at x = 1.25
first_derivative_125 = newton_forward_derivative(x_data, y_data, 1.25, 1)
second_derivative_125 = newton_forward_derivative(x_data, y_data, 1.25, 2)

# Calculate derivatives at x = 1.15
first_derivative_115 = newton_forward_derivative(x_data, y_data, 1.15, 1)
second_derivative_115 = newton_forward_derivative(x_data, y_data, 1.15, 2)

print("Derivatives at x = 1.05:")
print("First derivative:", first_derivative_105)
print("Second derivative:", second_derivative_105)

print("\nDerivatives at x = 1.25:")
print("First derivative:", first_derivative_125)
print("Second derivative:", second_derivative_125)

print("\nDerivatives at x = 1.15:")
print("First derivative:", first_derivative_115)
print("Second derivative:", second_derivative_115)