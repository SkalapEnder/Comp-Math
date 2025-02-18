from math import log, exp
from Gauss import gauss_elimination
import matplotlib.pyplot as plt

data_1 = [(0, 1), (1, 1.8), (2, 1.3), (3, 2.0), (4, 6.3)]
data_2 = [(6, 5), (7, 5), (7, 4), (8, 5), (8, 4), (8, 3), (9, 4), (9, 3), (10, 3)]
data_3 = [(0, 1.05), (1, 2.1), (2,  3.85), (3 , 8.3)]
data_4 = [(1, 1.8), (2, 5.1), (3, 8.9), (4, 14.1), (5, 19.8)]
data_5 = [(1, 5.4), (2, 6.3), (3, 8.2), (4, 10.3), (5, 12.6), (6, 14.9), (7, 17.3), (8, 19.5)]   

x_values_1 = [point[0] for point in data_1]
y_values_1 = [point[1] for point in data_1]

x_values_2 = [point[0] for point in data_2]
y_values_2 = [point[1] for point in data_2]

x_values_3 = [point[0] for point in data_3]
y_values_3 = [point[1] for point in data_3]

x_values_4 = [point[0] for point in data_4]
y_values_4 = [point[1] for point in data_4]

x_values_5 = [point[0] for point in data_5]
y_values_5 = [point[1] for point in data_5]

# Functions
def specific_parabola(x, a, b):
    return a * x + b * (x ** 2)

def another_parabola(x, a, b):
    return (a * x) + (b / x)

def second_degree_parabola(x, a, b, c):
    return (float(c) * (float(x) ** 2)) + (float(b) * float(x)) + float(a)

def exponent(x, a, b):
    return a * exp(b * x)

def linear(x, m, b):
    return m*x + b

# Least Square Method
def summations(xs, ys, model):
    ln_y = [log(yi) if yi > 0 else 0 for yi in ys]

    sum_x = sum(xs)
    sum_x2 = sum(xi**2 for xi in xs)
    sum_x3 = sum(xi**3 for xi in xs)
    sum_x4 = sum(xi**4 for xi in xs)

    sum_y = sum(ys)

    sum_xy = sum(x * y for x, y in zip(xs, ys))
    sum_xx = sum(x * x for x in xs)
    sum_x2y = sum((xi**2) * yi for xi, yi in zip(xs, ys))

    sum_ln_y = sum(ln_y)
    sum_x_ln_y = sum(xi * lnyi for xi, lnyi in zip(xs, ln_y))
    match model:
        case 'linear':
            return  sum_x, sum_y, sum_xy, sum_xx
        case 'exponential':
            return sum_x, sum_y, sum_xy, sum_xx, sum_ln_y, sum_x_ln_y
        case 'second_degree_parabola':
            return sum_x, sum_x2, sum_x3, sum_x4, sum_y, sum_xy, sum_x2y

# Linear Model: y = mx + b 
def linear_model(x_data, y_data):
    n = len(x_data)
    sum_x, sum_y, sum_xy, sum_xx = summations(x_data, y_data, 'linear')
    
    # Calculate slope (m) and intercept (b)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    
    return m, b

# Second Degree Parabola Model: y = a + bx + cx^2
def second_degree_parabola_model(x_data, y_data):
    n = len(x_data)
    sum_x, sum_x2, sum_x3, sum_x4, sum_y, sum_xy, sum_x2y = summations(x_data, y_data, 'second_degree_parabola')
    
    A = [[n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3], 
        [sum_x2, sum_x3, sum_x4]]
    B = [sum_y, sum_xy, sum_x2y]
    
    coefficients = gauss_elimination(A, B)
    return coefficients[0], coefficients[1], coefficients[2]

# Specific Model: y = ax + bx^2
def specific_parabola_model(x_data, y_data):
    n = len(x_data)
    sum_x, sum_x2, sum_x3, sum_x4, sum_y, sum_xy, sum_x2y = summations(x_data, y_data, 'second_degree_parabola')
    
    A = [# a       b
        [sum_x2, sum_x3],
        [sum_x3, sum_xy] 
    ]
    B = [sum_xy, sum_x2y]
    
    coefficients = gauss_elimination(A, B)
    return coefficients[0], coefficients[1]

# Exponential Model: y = a * e^(b * x)
def exponential_model(x_data, y_data):
    n = len(x_data)
    sum_x, sum_y, sum_xy, sum_xx, sum_ln_y, sum_x_ln_y = summations(x_data, y_data, 'exponential')
    
    b = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_xx - sum_x**2)
    ln_a = (sum_ln_y - b * sum_x) / n
    a = exp(ln_a) 
    
    return a, b

# Another Parabola Model: y = ax + b/x
def another_parabola_model(x_data, y_data):
    n = len(x_data)
    sum_x, sum_y, sum_xy, sum_xx, _, _ = summations(x_data, y_data, 'exponential')
    sum_1_x = sum(1 / xi for xi in x_data)
    sum_y_div_x = sum(yi / xi for xi, yi in zip(x_data, y_data))
    
    A = [
        [sum_xx, sum_x], # With respect to a
        [sum_x, sum_1_x] # With respect to b
    ]
    B = [sum_xy, sum_y_div_x]

    coeffs = gauss_elimination(A, B)
    return coeffs[0], coeffs[1]

# Plot the model graph
def plot_graph(x_data, y_data, a, b, equation, model, title):
    x_curve = [x for x in range(min(x_data), max(x_data) + 1)]
    y_curve = [model(x, a, b) for x in x_curve]
    
    # Plot the data points (dots)
    plt.scatter(x_data, y_data, color='red', label='Data points')
    
    # Plot the curve
    plt.plot(x_curve, y_curve, color='blue', label=equation)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{title} Model Curve with Data Points')
    plt.legend()
    
    plt.show()

def plot_graph_1(x_data, y_data, a, b, c, equation, title):
    x_curve = [x for x in range(min(x_data), max(x_data) + 1)]
    y_curve = [second_degree_parabola(x, a, b, c) for x in x_curve]
    
    # Plot the data points (dots)
    plt.scatter(x_data, y_data, color='red', label='Data points')
    
    # Plot the curve
    plt.plot(x_curve, y_curve, color='blue', label=equation)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{title} Model Curve with Data Points')
    plt.legend()
    
    plt.show()

# Fit the models
# Task 1
a, b, c = second_degree_parabola_model(x_values_1, y_values_1)
parab_eq = f"y = {c:.2f}x^2 + {b:.2f}x + {a:.2f}"
print(f"Second Degree Parabola Model (Task 1): {parab_eq}")
plot_graph_1(x_values_1, y_values_1, a, b, c, parab_eq, 'Second Degree Parabola')

# Task 2
a_2, b_2 = linear_model(x_values_2, y_values_2)
lin_eq = f"y = {a_2:.2f}x + {b_2:.2f}"
print(f"Linear Model (Task 2): {lin_eq}")
plot_graph(x_values_2, y_values_2, a_2, b_2, lin_eq, linear, 'Linear')

# Task 3
m_exp, b_exp = exponential_model(x_values_3, y_values_3)
exp_eq = f"y = {m_exp:.2f} * e^({b_exp:.2f} * x)"
print(f"Exponential Model (Task 3): {exp_eq}")
plot_graph(x_values_3, y_values_3, m_exp, b_exp, exp_eq, exponent, 'Exponential')

# Task 4
a_4, b_4 = specific_parabola_model(x_values_4, y_values_4)
spec_eq = f"y = {a_4:.2f}x + {b_4:.2f}x^2"
print(f"(y = ax + bx^2) Model (Task 4): {spec_eq}")
plot_graph(x_values_4, y_values_4, a_4, b_4, spec_eq, specific_parabola, 'y = ax + bx^2')

# Task 5
a_5, b_5 = specific_parabola_model(x_values_5, y_values_5)
another_eq = f"y = {a_5:.2f}x + {b_5:.2f}/x"
print(f"(y = ax + b/x) Model (Task 5): {another_eq}")
plot_graph(x_values_5, y_values_5, a_5, b_5, another_eq, another_parabola, 'y = ax + b/x')
