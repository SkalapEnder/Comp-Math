import numpy as np

def f(x): 
    return x**3 + x**2 - 1

def false_position(a, b, precision, max_iters, goal):
    result_list = []
    error_list = []
    iters = 0

    while iters < max_iters:
        x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        eps = abs(x - a)

        result_list.append([iters+1, x])
        error_list.append([iters+1, eps])
        
        if eps < precision:
            break

        if f(a) * f(x) < goal:
            b = x
        else:
            a = x
            
        iters += 1
    
    return result_list, error_list

def falsePos(precision, max_iters, goal):
    print("False position method")
    a = float(input("Write a: "))
    b = float(input("Write b: "))
    
    
    result_list, epsilon_list = false_position(a, b, precision, max_iters+1, goal) 

    return result_list, epsilon_list