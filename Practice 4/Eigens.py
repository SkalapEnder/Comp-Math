import numpy as np

A = [[2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]]

eigenvalue, eigenvector = np.linalg.eig(A) 
if eigenvalue.any() and eigenvector.any():
    print("Eigenvalue: ", eigenvalue)
    print("Eigenvector: ", eigenvector)
else:
    print("There is no eigens for this matrix!")