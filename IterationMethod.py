import numpy as np

goal = 0

def f(x): 
    return x**3 + x**2 - 1

def phi(x):
    return (1 + x) ** (-1/2)

def iterative_method(a, precision, max_iters):
    result_list = []
    error_list = []
    iters = 0

    while iters < max_iters:
        x = phi(a)

        if x == None:
            break
        
        eps = abs(x - a)

        result_list.append([iters+1, x])
        error_list.append([iters+1, eps])

        if eps < precision:
            break

        a = x

        iters += 1
    return result_list, error_list

def iterative(precision, max_iters, goalM):
    goal = goalM
    
    print("Iteration Method")
    a = float(input("Write x0: "))
    
    result_list, epsilon_list = iterative_method(a, precision, max_iters+1) 
    
    return result_list, epsilon_list