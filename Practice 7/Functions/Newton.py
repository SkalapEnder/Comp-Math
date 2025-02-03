def newton_cotes(f, a, b, n, degree):
    if n % degree != 0:
        raise ValueError(f"Number of intervals (n) must be a multiple of {degree}.")

    h = (b - a) / n  # Step size
    integral = 0

    # Define weights based on the degree of the polynomial
    if degree == 1:
        # Trapezoidal Rule
        weights = [1, 1]
    elif degree == 2:
        # Simpson's 1/3 Rule
        weights = [1, 4, 1]
    elif degree == 3:
        # Simpson's 3/8 Rule
        weights = [1, 3, 3, 1]
    elif degree == 4:
        # Boole's Rule
        weights = [7, 32, 12, 32, 7]
    elif degree == 6:
        # Weddle's Rule
        weights = [1, 5, 1, 6, 1, 5, 1]
    else:
        raise ValueError("Unsupported degree for Newton-Cotes formula.")

    # Apply the formula
    for i in range(0, n, degree):
        points = [a + (i + j) * h for j in range(degree + 1)]
        integral += sum(w * f(x) for w, x in zip(weights, points))

    # Multiply by the step size and normalization factor
    if degree == 1:
        integral *= h / 2
    elif degree == 2:
        integral *= h / 3
    elif degree == 3:
        integral *= 3 * h / 8
    elif degree == 4:
        integral *= 2 * h / 45
    elif degree == 6:
        integral *= 3 * h / 10

    return integral

if __name__ == "__main__":
    def f(x):
        return x**2

    a = 0 
    b = 1
    n = 6 
    degree = 2  # Degree of polynomial (2 for Simpson's 1/3 Rule)

    result = newton_cotes(f, a, b, n, degree)
    print(f"The approximate integral using Newton-Cotes (degree {degree}) is: {result}")