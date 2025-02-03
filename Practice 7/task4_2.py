from Functions.Simpson13 import simpsons_13_rule
from Functions.Simpson38 import simpsons_38_rule
from Functions.Trapezoid import trapezoid_rule
from Graph import plot_graph

if __name__ == "__main__":
    def f(x):
        return 1 / (1 + x)
    
    def f_der(x):
        return 24 / ((x + 1) ** 5)
    
    a = 0
    b = 1
    n = 10
    
    result, error = trapezoid_rule(f, a, b, n)
    print("Task 4 - i (Trapezoid)")
    print(f"Approximate integral of f(x) = 1 / (1 + x) from {a} to {b} is: {result}")
    print(f"Approximate error is: {error}")
    print()
    
    result, error = simpsons_13_rule(f, f_der, a, b, n)
    print("Task 4 - ii (Simpson's 1/3) +++")
    print(f"Approximate integral of f(x) = 1 / (1 + x) from {a} to {b} is: {result}")
    print(f"Approximate error is: {error}")
    print()
    
    result = simpsons_38_rule(f, a, b)
    print("Task 4 - iii (Simpson's 3/8)")
    print(f"Approximate integral of f(x) = 1 / (1 + x) from {a} to {b} is: {result}")
    print(f"Approximate error is: {error}")
    print()
    print(f"Approximate real answer of f(x) = 1 / (1 + x) from {a} to {b} is:: 0.6931471805599453")
    
    plot_graph(f, a, b, '1 / (1 + x)', n)