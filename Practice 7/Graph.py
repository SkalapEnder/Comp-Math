import matplotlib.pyplot as plt
import numpy as np

def plot_graph(f, a, b, name, n=10, n_max=10000):   
    x_values = []
    for x in np.linspace(a, b, n):
        x_values.append(x)

    y_values = []
    for x in x_values:
        y_values.append(f(x))
        
    x_values_ext = []
    for x in np.linspace(a, b, n_max):
        x_values_ext.append(x)
        
    y_values_ext = []
    for x in x_values_ext:
        y_values_ext.append(f(x))

    # 3. Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=name, color="blue")
    plt.plot(x_values_ext, y_values_ext, label=f"$Extended {name}$", color="red")
    plt.title(f"Graph of ${name}$")
    plt.xlabel("$x$")
    plt.ylabel(f"${name}$")
    plt.grid(True)
    plt.legend()
    plt.show()
    