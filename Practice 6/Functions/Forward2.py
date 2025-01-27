def forward_difference_table(data):
    x_values = [point[0] for point in data]
    y_values = [point[1] for point in data]
    h = x_values[1] - x_values[0]

    n = len(x_values)
    difference_table = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        difference_table[i][0] = y_values[i]

    # Compute forward differences
    for col in range(1, n):
        for row in range(n - col):
            difference_table[row][col] = difference_table[row + 1][col - 1] - difference_table[row][col - 1]
    return difference_table

def forward_difference_table(x_values, y_values):
    h = x_values[1] - x_values[0]

    n = len(x_values)
    difference_table = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        difference_table[i][0] = y_values[i]

    # Compute forward differences
    for col in range(1, n):
        for row in range(n - col):
            difference_table[row][col] = difference_table[row + 1][col - 1] - difference_table[row][col - 1]
    return difference_table