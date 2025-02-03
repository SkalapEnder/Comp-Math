def simpsons_38_rule(f, a, b):
    h = (b - a) / 3
    x0 = a
    x1 = a + h
    x2 = a + 2 * h
    x3 = b

    integral = (3 * h / 8) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3))
    return integral

if __name__ == "__main__":
    def f(x):
        return x**2 

    a = 0 
    b = 1

    result = simpsons_38_rule(f, a, b)
    print(f"The approximate value of the integral is: {result}")