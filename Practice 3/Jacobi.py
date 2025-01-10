import matplotlib.pyplot as plt

def jacobi_iteration(A, b, x0, tol=1e-6, max_iters=100):
    n = len(b)
    x = x0[:]
    result_list = [[],[],[],[]]
    epsilon_list = [[],[],[],[]]

    for iteration in range(max_iters):
        x_new = x[:]

        result_list[0].append(iteration)
        epsilon_list[0].append(iteration)
        for i in range(n):
            sum_terms_1 = sum(A[i][j] * x[j] for j in range(n) if j != i)

            x_new[i] = (b[i] - sum_terms_1) / A[i][i]
            result_list[i+1].append(x_new[i])
        
        for i in range(n):
            epsilon_list[i+1].append(abs(x_new[i] - x[i]))

        # Error tolerance (everything must be less than tolerance)
        if max([abs(x_new[i] - x[i]) for i in range(n)]) < tol:
            return x_new, result_list, epsilon_list

        x = x_new
    
    return x, result_list, epsilon_list

def print_2lists(result, epsilon):
    print('Iters\t \033[32mSolution (Xi, Yi, Zi)\033[0m\t\t\t\033[31mError (Xi, Yi, Zi)\033[0m')

    n = len(result[0])
    for i in range(len(result[0])):
        print(result[0][i], '\t| \033[32m', result[1][i], ' ', result[2][i], ' ', result[3][i], '\033[0m\t| \033[31m', epsilon[1][i], ' ', epsilon[2][i], ' ', epsilon[3][i], '\033[0m')
    
    print("Last one is rounded")
    print(result[0][n-1], '\t| \033[32m', round(result[1][n-1], 7), ' ', round(result[2][n-1], 7), ' ', round(result[3][n-1], 7), '\033[0m\t| \033[31m', round(epsilon[1][n-1], 12), ' ', round(epsilon[2][n-1], 12), ' ', round(epsilon[3][n-1], 12), '\033[0m')

def print_graph(data, a, b, c, general):
    plt.figure(figsize=(8, 6))

    iterations = data[0]
    xi = data[1]
    yi = data[2]
    zi = data[3]

    # Plot xi, yi, and zi with different colors
    plt.plot(iterations, xi, 'bo-', label=a)
    plt.plot(iterations, yi, 'ro-', label=b)
    plt.plot(iterations, zi, 'go-', label=c)

    # Set plot labels and title
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title('Iteration vs. ' + general)

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()


A = [[20., 1., -2.],
     [3., 20., -1.],
     [2., -3., 20.]
]
b = [17., -18., 25.]
x0 = [0, 0, 0]

solution, result_list, epsilon_list = jacobi_iteration(A, b, x0)

if solution is not None:
    print("Solution:", [round(val, 4) for val in solution])
    print_2lists(result_list, epsilon_list)

    print_graph(result_list, 'xi', 'yi', 'zi', 'Answer')
    print_graph(epsilon_list, 'Error xi', 'Error yi', 'Error zi', 'Error')
else:
    print("Convergence not reached.")