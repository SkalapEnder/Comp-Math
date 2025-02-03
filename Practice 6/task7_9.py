def f(x):
  result = 1
  for i in range(1, 16, 2):
    result *= (2 * x + i)
  return result

def delta(f, x, degree):
    if degree == 0: 
        return f(x)  # Base case
    else:
        print(f'Delta ^ {degree} f = ', (delta(f, x + 1, degree - 1) - delta(f, x, degree - 1)))
        return delta(f, x + 1, degree - 1) - delta(f, x, degree - 1)

x = 2
degree = 4
result = delta(f, x, degree)
print(f"Δ^{degree} f({x}) = {result}")