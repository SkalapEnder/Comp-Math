import numpy as np

def f(x): 
    return x**3 + x**2 - 1

def newton_method(a, precision, max_iters, goal):
    result_list = []
    error_list = []
    iters = 0
    h = 1e-6

    while iters < max_iters:
        df = (f(a + h) - f(a - h)) / (2 * h)

        x = a - (f(a) / df)
        eps = abs(x - a)

        result_list.append([iters+1, x])
        error_list.append([iters+1, eps])

        if eps < precision:
            break

        a = x

        iters += 1

    return result_list, error_list

def newton(precision, max_iters, goal):
    print("Newton Method")
    a = float(input("Write x0: "))
    
    result_list, epsilon_list = newton_method(a, precision, max_iters+1 , goal) 
    
    return result_list, epsilon_list