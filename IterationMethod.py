import math
import matplotlib.pyplot as plt

goal = 1

def f(x): 
    return x * (math.e ** x)

def phi(x):
        return (math.e ** (-x))

def iterative_method(a, precision, max_iters):
    result_list = []
    error_list = []
    iters = 0

    while iters < max_iters:
        x = phi(a)
        eps = abs(x - a)

        result_list.append([iters+1, x])
        error_list.append([iters+1, eps])

        if eps < precision:
            break

        a = x

        iters += 1
    return result_list, error_list

def main():
    precision = 1e-20
    max_iters = 100

    a = float(input("Write x0: "))
    
    result_list, epsilon_list = iterative_method(a, precision, max_iters+1) 
    
    for iteration, answer in result_list:
        print(f"Iteration {iteration}: Answer = {answer}")
    outputGraph(result_list, 'Answer')
    
    for iteration, epsilon in epsilon_list:
        print(f"Iteration {iteration}: Epsilon = {epsilon}")
    outputGraph(epsilon_list, 'Epsilon')

def outputGraph(array_list, name):
    iterations, answers = zip(*array_list)  

    plt.plot(iterations, answers, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel(name)
    plt.title('Iterative Method: Iteration vs. ' + name)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()