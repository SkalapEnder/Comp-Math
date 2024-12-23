import math
import matplotlib.pyplot as plt

goal = 0

def f(x): 
    return x * math.sin(x)

def false_position(a, b, precision, max_iters):
    result_list = []
    error_list = []
    iters = 0

    while iters < max_iters:
        x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        eps = abs(x - a)
        print(eps)
        if eps < precision:
            break
        
        result_list.append([iters+1, x])
        error_list.append([iters+1, eps])

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
            
        iters += 1
    
    return result_list, error_list

def main():
    precision = 1e-20
    max_iters = 100
    print("Function: x * sin(x) = ", goal)
    a = float(input("Write a: "))
    b = float(input("Write b: "))
    
    
    result_list, epsilon_list = false_position(a, b, precision, max_iters+1) 
    
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
    plt.title('False Position Method: Iteration vs. ' + name)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()