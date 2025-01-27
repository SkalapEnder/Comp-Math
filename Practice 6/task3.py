from Functions.Forward2 import forward_difference_table

def print_table(table):
    print("\nDifference Table:")
    print(f"{'x':<10}{'f(x)':<10}", end="")

    for i in range(1, n):
        print(f"∇^{i}f{'':<5}", end="")
    print()

    for row in range(n):
        for col in range(n):
            if table[row][col] is not None:
                print(f"{table[row][col]:<10.2f}", end="")
            else:
                print(f"{'':<10}", end="")
        print()

def y_function(x):
    return (x ** 3) + (x ** 2) - (2 * x) + 1

x_values = [0, 1, 2, 3, 4, 5]
y_values = [y_function(x) for x in x_values]

n = len(y_values)

difference_table = forward_difference_table(x_values, y_values)

first_row_differences = [difference_table[0][i] for i in range(n) if difference_table[0][i] is not None]

h = x_values[1] - x_values[0]  # Step size
x_start = x_values[0] 
y_start = y_values[0] 

# Calculate y(6) using forward differences
x_target = 6
u = (x_target - x_start) / h  # u = (x - x0) / h
y_extrapolated = y_start
term = 1
factorial = 1

for i in range(1, len(first_row_differences)):
    term *= (u - (i - 1))
    factorial *= i
    y_extrapolated += (term / factorial) * first_row_differences[i]

# Step 4: Verify by substitution
y_direct = y_function(x_target)

print_table(difference_table)
print(y_extrapolated, y_direct)