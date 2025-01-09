import numpy as np
import Determinant as det

def checkInversing(matrix):
    if det.determinant(matrix) == 0:
        return False
    else: return True

def inversing(matrix):
    if not checkInversing(matrix):
        print("Matrix is not invertible!")
        return None

    
    return None


A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

In = inversing(A)
if In != None:
    print("Inverse matrix")
    print_matrix(In)
else:
    print("There is no inverse for this matrix!")

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, ' ')
        print('\n')