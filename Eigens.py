import numpy as np

def power_method(A, tol=1e-6, max_iter=1000):
  """
  Находит собственное значение с наибольшим модулем и соответствующий собственный вектор методом степеней.

  Args:
    A: Исходная матрица (numpy.ndarray)
    tol: Точность (по умолчанию 1e-6)
    max_iter: Максимальное число итераций

  Returns:
    Кортеж из собственного значения и собственного вектора.
  """

  n = A.shape[0]
  x = np.random.rand(n)  # Случайный начальный вектор

  for _ in range(max_iter):
    y = np.dot(A, x)
    lambda_ = np.dot(y, x) / np.dot(x, x)
    x = y / np.linalg.norm(y)

    if np.linalg.norm(y - lambda_ * x) < tol:
      return lambda_, x

  return None, None

# Пример использования
A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]])

eigenvalue, eigenvector = power_method(A)
print("Собственное значение:", eigenvalue)
print("Собственный вектор:", eigenvector)