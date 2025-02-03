from math import pi, sin
from Functions.Simpson38 import simpsons_38_rule
from Graph import plot_graph

def f1(x):
    return 1 / (1 + x**3)

def f2(x):
    return sin(x)

a = 0
b = 9

result = simpsons_38_rule(f1, a, b)
print("Task 3 - i")
print(f"Approximate integral of f(x) = sin(x) from {a} to {b} is: {result}")
print(f"Approximate result is: {result:.2f}")
print()
plot_graph(f1, a, b, '1 / (1 + x ** 3)')

a = 0
b = pi / 2

result = simpsons_38_rule(f2, a, b)
print("Task 3 - ii")
print(f"Approximate integral of f(x) = sqrt(cos(x))dx from {a} to {b} is: {result}")
print(f"Approximate result is: {result:.2f}")
plot_graph(f2, a, b, 'sin(x)')