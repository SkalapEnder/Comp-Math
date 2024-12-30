import numpy as np

def f(x): 
    return x**3 + x**2 - 1

def bisection_method(a, b, precision, max_iters, goal):
    result_list = []
    error_list = []
    iters = 0

    while iters < max_iters:
        x = (a + b) * 0.5
        err = abs(x - a)
        
        result_list.append([iters, x])
        error_list.append([iters, err])
        
        if err < precision:
            break
        
        if f(x) * f(b) < goal:
            a = x
        else:
            b = x
            
        iters += 1

    return result_list, error_list


def bisection(precision, max_iters, goal):
    print("Bisection method")
    print("Function: x**3 + x**2 - 1 = ", goal)
    a = float(input("Write a: "))
    b = float(input("Write b: "))

    result_list, epsilon_list = bisection_method(a, b, precision, max_iters+1, goal) 
    
    return result_list, epsilon_list
