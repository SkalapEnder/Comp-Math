def booles_rule(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("Number of intervals (n) must be a multiple of 4.")
    
    h = (b - a) / n
    integral = 0
    
    for i in range(0, n, 4):
        x0 = a + i * h
        x1 = x0 + h
        x2 = x1 + h
        x3 = x2 + h
        x4 = x3 + h
        
        integral += 7 * f(x0) + 32 * f(x1) + 12 * f(x2) + 32 * f(x3) + 7 * f(x4)
    
    integral *= 2 * h / 45
    return integral

if __name__ == "__main__":
    def f(x):
        return x**2 

    a = 0
    b = 1 
    n = 8 

    result = booles_rule(f, a, b, n)
    print(f"The approximate integral using Boole's Rule is: {result}")