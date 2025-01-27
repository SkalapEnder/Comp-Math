def lagrange_interpolation(data, x_interp):
    x = [point[0] for point in data]
    y = [point[1] for point in data]

    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= ((x_interp - x[j]) / (x[i] - x[j]))
        result += term
    return result