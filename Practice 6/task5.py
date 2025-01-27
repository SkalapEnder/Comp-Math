def extend_table(x_values, y_values, num_extensions=2):
    n = len(x_values)
    h = x_values[1] - x_values[0] 

    # Create the difference table
    diff_table = []
    for col in range(1, n):
        for row in range(n - col):
            diff_table[row][col] = diff_table[row + 1][col - 1] - diff_table[row][col - 1]


    # Extend the table to the left
    extended_x_values = x_values[:].copy()
    extended_y_values = y_values[:].copy()
    for _ in range(num_extensions):
        extended_x_values.insert(0, extended_x_values[0] - h)
        new_y = extended_y_values[0]
        for i in range(1, n):
            new_y -= diff_table[i][0]
        extended_y_values.insert(0, new_y)

    # Extend the table to the right
    for _ in range(num_extensions):
        extended_x_values.append(extended_x_values[-1] + h)
        new_y = extended_y_values[-1]
        for i in range(1, n):
            new_y += sum(diff_table[j][-1] for j in range(i))
        extended_y_values.append(new_y)

    return extended_x_values, extended_y_values


x_values = [-0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_values = [2.6, 3.0, 3.4, 4.28, 7.08, 14.2, 29.0]

extended_x, extended_y = extend_table(x_values, y_values, num_extensions=2)

print("Extended x-values:", extended_x)
print("Extended y-values:", extended_y)