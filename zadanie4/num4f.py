import matplotlib.pyplot as plt
import time
import numpy as np

def sherman(matrix, b, n):
    y = []
    q = [0] * n
    w = [0] * n
    q[n - 1] = b[n - 1] / matrix[0][n - 1]

    # Obliczenia dla q (rozwiązanie układu dla b)
    for i in range(n - 2, -1, -1):
        q[i] = (b[i] - matrix[1][i] * q[i + 1]) / matrix[0][i]

    # Obliczenia dla w (rozwiązanie układu dla prawej strony jednostkowej)
    w[n - 1] = 1 / matrix[0][n - 1]
    for i in range(n - 2, -1, -1):
        w[i] = (1 - matrix[1][i] * w[i + 1]) / matrix[0][i]

    delta = sum(q) / (1 + sum(w))

    # Wyliczenie wyniku
    for i in range(n):
        y.append(q[i] - w[i] * delta)

    return y

# Parametry zadania
n = 120
matrix = []
matrix.append([5] * n)
matrix.append([3] * (n - 1) + [0])
b = [2] * n

# Rozwiązanie własną funkcją
y_custom = sherman(matrix, b, n)

# Sprawdzenie wyniku za pomocą numpy
A = np.diag([5] * n) + np.diag([3] * (n - 1), 1) + np.ones((n, n))
y_numpy = np.linalg.solve(A, b)

# Wyświetlenie różnic między wynikami
difference = np.array(y_custom) - y_numpy
print("Różnice między rozwiązaniami własnej funkcji a numpy:", difference)

# Pomiar czasu dla różnych wymiarów macierzy
N_values = range(10, 10000, 50)
times = []
for N in N_values:
    start_time = time.time()
    matrix = [[5] * N, [3] * (N - 1) + [0]]
    b = [2] * N
    sherman(matrix, b, N)
    times.append(time.time() - start_time)

# Wykres czasu w zależności od rozmiaru macierzy
plt.plot(N_values, times, )
plt.grid(True)
plt.xlabel("Rozmiar macierzy N")
plt.ylabel("Czas rozwiązania [s]")
plt.title("Czas rozwiązania w funkcji rozmiaru N")
plt.show()
