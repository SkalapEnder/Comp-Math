def trapezoid_rule(f, a, b, n):
    h = (b - a) / n

    integral = 0.5 * (f(a) + f(b)) 

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h
    
    max_f_double_prime = max(abs(6*x) for x in [a, b])  # Approximate max
    error = ((b - a) ** 3) / (12 * n**2) * max_f_double_prime
    
    return integral, error

def trapezoid_rule(f, f_der, a, b, n):
    h = (b - a) / n

    integral = 0.5 * (f(a) + f(b)) 

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h
    
    max_f_fourth_prime = 0
    max_f_double_prime = max(abs(f_der(x)) for x in [a, b])  # Approximate max
    if max_f_fourth_prime < 0.01: max_f_fourth_prime = 1
    error = (-(b - a) ** 3) / (12 * n**2) * max_f_double_prime
    
    return integral, error


if __name__ == "__main__":
    def f(x):
        return x**3 
    
    def f_der(x):
        return 6*x

    a = 0
    b = 1
    n = 16
    
    result, error = trapezoid_rule(f, f_der, a, b, n)
    print(f"Approximate integral of f(x) = x^3 from {a} to {b} is: {result:.8f}")
    print(f"Error: {(error):.8f}")
    print(f"Nearest value of integral: 0.25")