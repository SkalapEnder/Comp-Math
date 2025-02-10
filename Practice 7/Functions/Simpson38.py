def simpsons_38_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Number of intervals (n) must be even.")
    
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    integral = f(x[0]) + f(x[-1])
    
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * f(x[i])
        else:
            integral += 3 * f(x[i])
    
    integral *= (3 * h / 8)
    
    error = ((b - a) * h**4 / 80) * max(abs(f(x_i)) for x_i in x)
    return integral, error

if __name__ == "__main__":
    def f(x):
        return x**3 
    
    a = 0 
    b = 1
    n = 15

    result, error = simpsons_38_rule(f, a, b, n)
    print(f"The approximate value of the integral is: {result}")
    print(f"The approximate value of the error is: {error}")