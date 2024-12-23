import math
import matplotlib.pyplot as plt

goal = 0

def f(x): 
    return x * math.sin(x)

def iterative_method(a, b, precision, max_iters):
    result_list = []
    error_list = []
    iters = 0

    while iters < max_iters:
        print()
    return result_list, error_list

def main():
    precision = 1e-20
    max_iters = 100

    a = float(input("Write x0: "))
    
    result_list, epsilon_list = iterative_method(a, b, precision, max_iters+1) 
    
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