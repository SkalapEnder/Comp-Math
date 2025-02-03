from Functions.Terms import lagrange_interpolation

def forward_interpolation(data, x_interp):
    x = [point[0] for point in data]
    y = [point[1] for point in data]
  
    n = len(x)

    diff_table = forward_difference_table(data) 

    # Calculate u
    h = x[1] - x[0]
    u = (x_interp - x[0]) / h

    # Initialize result
    result = diff_table[0][0]

    # Calculate interpolated value using forward difference formula
    term = 1
    for i in range(1, n):
        term *= (u - i + 1) / i
        result += term * diff_table[i][0]

    return result

def forward_difference_table(data):
    x_values = [point[0] for point in data]
    f_values = [point[1] for point in data]

    n = len(f_values)
    table = [[None] * (n + 1) for _ in range(n)]

    for i in range(n):
        table[i][0] = x_values[i]
        table[i][1] = f_values[i]

    for col in range(2, n + 1):
        for row in range(n - col + 1):
            table[row][col] = table[row + 1][col - 1] - table[row][col - 1]
    
    return table

data = [(2, 45.0), (3, 49.2), (4, 54.1)]
x_interp = 5

# y_interp = forward_interpolation(data, x_interp)
print("Task 6 & 10")
# print(f"\nP({x_interp:.2f}) = {y_interp:.2f}") 

y_interp = lagrange_interpolation(data, x_interp)
print(f"\nP({x_interp:.2f}) = {y_interp:.2f}") 
