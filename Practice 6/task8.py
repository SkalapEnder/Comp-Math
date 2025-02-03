def forward_differences(x_values, y_values):
    n = len(y_values)
    table = [y_values.copy()] # To first row
    
    # Compute forward differences iteratively
    for i in range(1, n):
        row = []
        for j in range(len(table[-1]) - 1):
            row.append(table[-1][j + 1] - table[-1][j])
        table.append(row)
    
    return table

def evaluate_polynomial(x_values, forward_diff_table, x):
    n = len(x_values)
    h = x_values[1] - x_values[0] # Step
    u = (x - x_values[0]) / h # Normalized distance

    y = forward_diff_table[0][0]
    u_term = 1

    # y = y0 + u * del^1 y0 + (u(u-1)/2!) * del^2 y0 + ...
    for i in range(1, n):
        u_term *= (u - (i - 1)) / i # Update factorial and add new (u - i)
        y += u_term * forward_diff_table[i][0] # del^n y0
    return y

def print_table(x_values, y_values, forward_diff_table):
    print("\nDifference Table")
    print(f"{'x':<8}{'f(x)':<8}", end="")
    for i in range(1, len(forward_diff_table)):
        print(f"Δ^{i}f", end="\t")
    print()
    
    for i in range(len(x_values)):
        print(f"{x_values[i]:<8.2f}{y_values[i]:<8.2f}", end="")
        
        for j in range(1, len(forward_diff_table)):
            if i < len(forward_diff_table[j]):
                print(f"{forward_diff_table[j][i]:<8.2f}", end="")
            else:
                print(" " * 8, end="")
        print()

x_values = [0, 1, 2, 3, 4]
y_values = [1, -1, 1, -1, 1]

forward_diff_table = forward_differences(x_values, y_values)

for x in range(5, 7 + 1):
    y = evaluate_polynomial(x_values, forward_diff_table, x)
    print(f"x = {x}, y = {y}")
    
print_table(x_values, y_values, forward_diff_table)
