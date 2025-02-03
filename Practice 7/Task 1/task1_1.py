def forward_difference_table(x_values, y_values):
    h = x_values[1] - x_values[0]

    n = len(x_values)
    difference_table = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        difference_table[i][0] = y_values[i]

    for col in range(1, n):
        for row in range(n - col):
            difference_table[row][col] = difference_table[row + 1][col - 1] - difference_table[row][col - 1]
            
    return difference_table


time = [0, 5, 10, 15]  # Time in seconds
velocity = [0, 3, 14, 69]  # Velocity in m/sec

difference_table = forward_difference_table(time, velocity)

initial_acceleration = float(difference_table[0][1] / (time[1] - time[0]))
print(f"Initial acceleration: {initial_acceleration:.2f} m/s^2")