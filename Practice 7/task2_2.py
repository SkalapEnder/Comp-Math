from math import pi, sin, cos, sqrt
from Functions.Simpson13 import simpsons_13_rule
from Graph import plot_graph

def f1(x):
    return sin(x)

def f1_2n(x):
    return cos(x)

def f2(x):
    return sqrt(cos(x))

def f2_4(x):
    return -(15 * sin(x)**4 + 20 * cos(x)**2 * sin(x)**2 + 4 * cos(x)**4) / (16 * cos(x)**(7 / 2))

a = 0
b = pi
n = 20 # num of ordinates (points) - 1 = nums of intervals

result, error = simpsons_13_rule(f1, f1_2n, a, b, n)
print("Task 2 - i")
print(f"Approximate integral of f(x) = sin(x) from {a} to {b} is: {result}")
print(f"Approximate error is: {error}")
print()
plot_graph(f1, a, b, 'sin(x)', n)

a = 0
b = pi / 2
n = 18 # num of ordinates (points) - 1 = nums of intervals

result, error = simpsons_13_rule(f2, f2_4, a, b, n)
print("Task 2 - ii")
print(f"Approximate integral of f(x) = sqrt(cos(x))dx from {a} to {b} is: {result}")
print(f"Approximate error is: {error}")
plot_graph(f2, a, b, 'sqrt(cos(x))', n)