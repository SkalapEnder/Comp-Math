import numpy as np

def gauss_elimination(A):
    """
    Реализует метод Гаусса для решения системы линейных уравнений.

    Args:
        A: Расширенная матрица системы (numpy.ndarray).

    Returns:
        Решение системы (numpy.ndarray) или None, если система не имеет единственного решения.
    """

    n = A.shape[0]

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента в столбце
        max_row = i + np.argmax(np.abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]

        # Деление строки на ведущий элемент
        if A[i, i] == 0:
            return None  # Система не имеет единственного решения

        A[i] /= A[i, i]

        # Обнуление элементов ниже ведущего
        for j in range(i + 1, n):
            A[j] -= A[j, i] * A[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = A[i, -1] - np.dot(A[i, :n-1], x[i+1:])

    return x

# Пример использования
A = np.array([[2, -1, 1, 8],
              [1, 3, 1, 1],
              [3, -2, 2, 9]])

solution = gauss_elimination(A)
if solution is not None:
    print("Решение системы:", solution)
else:
    print("Система не имеет единственного решения.")