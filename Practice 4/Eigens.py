import numpy as np

def eigens(A):

  return None, None


A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

eigenvalue, eigenvector = eigens(A)
if eigenvalue != None and eigenvector != None:
    print("Eigenvalue: ", eigenvalue)
    print("Eigenvector: ", eigenvector)
else:
    print("There is no eigens for this matrix!")