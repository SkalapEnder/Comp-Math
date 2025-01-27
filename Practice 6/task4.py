def function_f(x):
  return x**3 + 5*x - 7

def create_difference_table(x_values):
  n = len(x_values)
  table = []
  for i in range(n):
    row = []
    for j in range(n - i):
      if i == 0:
        row.append(function_f(x_values[j]))
      else:
        row.append(table[i - 1][j + 1] - table[i - 1][j])
    table.append(row)
  return table

def print_difference_table(table):
    for row in table:
        print(row)


x_values = [-1, 0, 1, 2, 3, 4, 5]
difference_table = create_difference_table(x_values)
print_difference_table(difference_table)

# Extend the table to find f(6)
last_row = difference_table[-1]
extended_row = [last_row[-1]]  # Assuming constant higher-order differences

for i in range(len(last_row) - 1):
    extended_row.append(last_row[i])
difference_table.append(extended_row)

# Calculate f(6)
f6 = difference_table[0][-1] + sum(difference_table[i][-1] for i in range(1, len(difference_table)))
print(f"f(6) = {f6}")