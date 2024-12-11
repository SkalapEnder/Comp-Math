import math
import numpy as np
import matplotlib.pyplot as plt


def f(a):
    return a * math.sin(a)


def error_tolerance(precision, x1, x2):
    return abs(x1 - x2) > precision


def bisection_method(a, b, precision, max_iters):
    result_list = []
    iters = 0

    while error_tolerance(precision, a, b) and iters < max_iters:
        x = (a + b) * 0.5
        result_list.append([iters, x])
        
        if f(x) * f(b) < 0:
            a = x
        else:
            b = x
        iters += 1

    return result_list


def main():
    precision = 1e-10
    max_iters = 100

    a = float(input("Write a: "))
    b = float(input("Write b: "))

    result_list = bisection_method(a, b, precision, max_iters)

    for iteration, answer in result_list:
        print(f"Iteration {iteration}: Answer = {answer}")
    outputGraph_AnswerIteration(result_list)
    
   
def outputGraph_AnswerIteration(result_list):
    iterations, answers = zip(*result_list)  

    plt.plot(iterations, answers, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Answer')
    plt.title('Bisection Method: Iteration vs. Answer')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
