def y_function(x):
  return x**3 + 5*x - 7

def create_difference_table(x_values, y_values):
    n = len(x_values)
    table = [[None for _ in range(n - i)] for i in range(n)] 

    for i in range(n):
        for j in range(n - i):
            if i == 0:
                table[i][j] = y_values[j]
            else:
                table[i][j] = table[i - 1][j + 1] - table[i - 1][j]

    return table

def print_table(table):
    n = len(table)
    print("\nDifference Table:")
    print(f"{'f(x)':<10}", end="")

    for i in range(1, n):
        print(f"∇^{i}f{'':<5}", end="")
    print()

    for row in range(n):
        print(str(row)) 
        for col in range(n - row):
            if table[row][col] is not None:
                print(f"{table[row][col]:<10.2f}", end="")
            else:
                print(f"{'':<10}", end="")
        print()


x_values = [-1, 0, 1, 2, 3, 4, 5]
y_values = [y_function(x) for x in x_values]
difference_table = create_difference_table(x_values, y_values)
# print_table(difference_table)

# Extend the table to find f(6)
last_row = difference_table[-1]
extended_row = [last_row[-1]]  # Assuming constant higher-order differences

for i in range(len(last_row) - 1):
    extended_row.append(last_row[i])
difference_table.append(extended_row)

# Calculate f(6)
f6 = difference_table[0][-1] + sum(difference_table[i][-1] for i in range(1, len(difference_table)))
print(f"f(6) = {f6}")