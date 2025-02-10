def simpsons_13_rule(f, f_der, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of intervals (n) must be even.")
    
    h = (b - a) / n
    integral = f(a) + f(b) 
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    h = (b - a) / n
    max_f_fourth_prime = max(abs(f_der(x)) for x in [a, b])  # Approximate max
    if max_f_fourth_prime < 0.01: max_f_fourth_prime = 1
    error = (-(b - a) ** 5) / (180 * n**4) * max_f_fourth_prime
    
    integral *= h / 3
    return integral, error

if __name__ == "__main__":
    def f(x):
        return x**4
    
    def f_der(x):
        return 24.0 * (x - x + 1)

    a = 0 
    b = 1 
    n = 16

    result, error = simpsons_13_rule(f, 1, a, b, n)
    print(f"The approximate integral is: {result}")
    print(f"The approximate error is: {error}")