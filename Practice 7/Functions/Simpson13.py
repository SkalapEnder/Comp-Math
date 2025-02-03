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
    error = (b - a) / 180 * h**4 * max_f_fourth_prime
    
    integral *= h / 3
    return integral, error

if __name__ == "__main__":
    def f(x):
        return x**2

    a = 0 
    b = 1 
    n = 100

    result = simpsons_rule(f, a, b, n)
    print(f"The approximate integral is: {result}")