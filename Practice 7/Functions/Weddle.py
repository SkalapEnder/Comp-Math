def weddles_rule(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("Number of intervals (n) must be a multiple of 6.")
    
    h = (b - a) / n
    integral = 0
    
    for i in range(0, n, 6):
        x0 = a + i * h
        x1 = x0 + h
        x2 = x1 + h
        x3 = x2 + h
        x4 = x3 + h
        x5 = x4 + h
        x6 = x5 + h
        
        integral += f(x0) + 5 * f(x1) + f(x2) + 6 * f(x3) + f(x4) + 5 * f(x5) + f(x6)
    
    integral *= 3 * h / 10
    return integral

if __name__ == "__main__":
    def f(x):
        return x**2

    a = 0
    b = 1
    n = 12  # Number of intervals (must be a multiple of 6)

    result = weddles_rule(f, a, b, n)
    print(f"The approximate integral using Weddle's Rule is: {result}")