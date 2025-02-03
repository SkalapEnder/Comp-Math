def difference_table(data, output_table, output_step, way='Forward', ):
    x_values = [point[0] for point in data]
    f_values = [point[1] for point in data]
    h = x_values[1] - x_values[0]

    n = len(f_values) # Number of diffs = nums of f(x) - 1
    table = [[None] * (n + 1) for _ in range(n)]

    for i in range(n):
        table[i][0] = f_values[i]

    # Choose which differences we want to go
    match way:
        case 'Forward':
            # Compute forward differences
            print('\nForward Difference: Δf = f(x+h) - f(x)')
            for col in range(1, n):
                if output_step: print(f'\n Column (Δ^{col}f)\n')
                for row in range(n - col):
                    table[row][col] = table[row + 1][col - 1] - table[row][col - 1]
                    if output_step: print(f'{table[row][col]:.2f}\t| {table[row + 1][col - 1]:.2f}  -  {table[row][col - 1]:.2f}')
           
            # Print the table
            if output_table:
                print("\nForward Difference Table:")
                print(f"{'f(x)':<10}", end="")

                for i in range(1, n):
                    print(f"Δ^{i}f{'':<5}", end="")
                print()

                # Print values
                for row in range(n):
                    for col in range(n + 1):
                        if table[row][col] is not None:
                            print(f"{table[row][col]:<10.2f}", end="")
                        else:
                            print(f"{'':<10}", end="")
                    print()

        case 'Backward':
            # Compute backward differences
            print('\nBackward Difference: Δf = f(x) - f(x-h)')
            for col in range(1, n):
                if output_step: print(f'\n Column (∇^{col}f)\n')
                for row in range(col, n):
                    table[row][col] = table[row][col - 1] - table[row - 1][col - 1]
                    if output_step: print(f'{table[row][col]:.2f}\t| {table[row][col - 1]:.2f}  -  {table[row - 1][col - 1]:.2f}')

            if output_table:
                print("\nBackward Difference Table:")
                print(f"{'f(x)':<10}", end="")

                for i in range(1, n):
                    print(f"∇^{i}f{'':<5}", end="")
                print()

                for row in range(n):
                    for col in range(n + 1):
                        if table[row][col] is not None:
                            print(f"{table[row][col]:<10.2f}", end="")
                        else:
                            print(f"{'':<10}", end="")
                    print()
    return table