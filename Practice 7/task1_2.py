from Functions.Trapezoid import trapezoid_rule
from Graph import plot_graph

def f(x):
    return x**3 

a = 0
b = 1
n = 5

result, error = trapezoid_rule(f, a, b, n)
print(f"Approximate integral of f(x) = x^3 from {a} to {b} is: {result:.8f}")
print(f"Error: {error:.8f}")
print(f"Nearest value of integral: 0.25")
plot_graph(f, a, b, 'x^3', n)