def forward_difference_table(x, y):
    n = len(x)
    table = [[0] * n for _ in range(n)]
    table[0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    return table

def newton_forward_derivative(x, y, x_interp, order):
    h = x[1] - x[0] 
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
x_data = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
y_data = [3.375, 7.000, 13.625, 24.000, 38.875, 59.000]

# Calculate derivatives at x = 1.5
first_derivative = newton_forward_derivative(x_data, y_data, 1.5, 1)
second_derivative = newton_forward_derivative(x_data, y_data, 1.5, 2)
third_derivative = newton_forward_derivative(x_data, y_data, 1.5, 3)

print("Approximate first derivative at x = 1.5:", first_derivative)
print("Approximate second derivative at x = 1.5:", second_derivative)
print("Approximate third derivative at x = 1.5:", third_derivative)