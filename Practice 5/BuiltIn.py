import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the models
def linear(x, m, b):
    return m * x + b

def second_degree_parabola(x, a, b, c):
    return a + b * x + c * (x ** 2)

def specific_parabola(x, a, b):
    return a * x + b * (x ** 2)

def exponent(x, a, b):
    return a * np.exp(b * x)  # Use numpy.exp for vectorized operations

def another_parabola(x, a, b):
    # Avoid division by zero
    return np.where(x != 0, a * x + b / x, np.inf)

# Calculate residuals
def calculate_residuals(y_data, y_fitted):
    return np.sum((y_data - y_fitted) ** 2)

# Guess the best model
def guess_best_model(x_data, y_data):
    models = [
        ("Linear", linear),
        ("Second Degree Parabola", second_degree_parabola),
        ("Specific Parabola", specific_parabola),
        #("Exponential", exponent),
        ("Another Parabola", another_parabola)
    ]

    best_model = None
    best_residual = float('inf')
    best_fitted_curve = None
    best_coefficients = None

    for model_name, model_func in models:
        try:
            popt, _ = curve_fit(model_func, x_data, y_data)

            y_fitted = model_func(np.array(x_data), *popt)
            residuals = calculate_residuals(np.array(y_data), y_fitted)
            
            # Check if this model is better
            if residuals < best_residual:
                print("\nFound new parameters!\n")
                print(f"Old Residual: {best_residual}, New Residual: {residuals}")
                print(f"Old Model: {best_model}, New Model: {model_name}")
                best_residual = residuals
                best_model = model_name
                best_fitted_curve = y_fitted
                best_coefficients = popt
        except Exception as e:
            print(f"Model {model_name} failed with error: {e}")
            continue

    # Plot the data and the best fit
    plt.scatter(x_data, y_data, color='red', label="Data Points")
    if best_fitted_curve is not None:
        plt.plot(x_data, best_fitted_curve, color='blue', 
                 label=f"Best Fit: {best_model} (Residual: {best_residual:.2f})")
    plt.title("Best Model Fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

    return best_model, best_coefficients, best_residual

# Example usage with a dataset
data_2 = data_3 = [(0.1, 1.05), (1, 2.1), (2,  3.85), (3 , 8.3)]






















x_data = [point[0] for point in data_2]
y_data = [point[1] for point in data_2]

best_model, best_coefficients, best_residual = guess_best_model(x_data, y_data)
print(f"Best Model: {best_model}")
print(f"Coefficients: {best_coefficients}")
print(f"Residual: {best_residual}")
