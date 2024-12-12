import math
import numpy as np
import matplotlib.pyplot as plt


def f(a):
    return a * math.sin(a)


def error_tolerance(precision, x1, x2):
    return abs(x1 - x2) > precision


def bisection_method(a, b, precision, max_iters):
    result_list = []
    error_list = []
    iters = 0

    while error_tolerance(precision, a, b) and iters < max_iters:
        x = (a + b) * 0.5
        err = abs(x - b)
        result_list.append([iters, x])
        error_list.append([iters, err])
        
        if f(x) * f(b) < 0:
            a = x
        else:
            b = x
        iters += 1

    return result_list, error_list


def main():
    precision = 1e-7
    max_iters = 100

    a = float(input("Write a: "))
    b = float(input("Write b: "))

    result_list, error_list = bisection_method(a, b, precision, max_iters+1) 
    
    for iteration, answer in result_list:
        print(f"Iteration {iteration}: Answer = {answer}")
    outputGraph_AnswerIteration(result_list)
    
    for iteration, error in error_list:
        print(f"Iteration {iteration}: Error = {error}")
    outputGraph_ErrorIteration(error_list)
    
   
def outputGraph_AnswerIteration(result_list):
    iterations, answers = zip(*result_list)  

    plt.plot(iterations, answers, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Answer')
    plt.title('Bisection Method: Iteration vs. Answer')
    plt.grid(True)
    plt.show()

def outputGraph_ErrorIteration(error_list):
    iterations, answers = zip(*error_list)  

    plt.plot(iterations, answers, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Bisection Method: Iteration vs. Error')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
