import time
import matplotlib.pyplot as plt


def lufac(n):
    matrix = [[0] * n for _ in range(4)]
    matrix[0][1:] = [0.3] * (n - 1)
    matrix[1] = [1.01] * n
    matrix[2][:n - 1] = [0.2 / i for i in range(1, n)]
    matrix[3][:n - 2] = [0.15 / (i ** 3) for i in range(1, n - 1)]

    x = list(range(1, n + 1))

    for i in range(n):
        if i == 0:
            continue  # Pomijamy dla pierwszego elementu

        if i == n - 2:
            factor = matrix[0][n - 2] / matrix[1][n - 3]
            matrix[0][n - 2] = factor
            matrix[1][n - 2] -= factor * matrix[2][n - 3]
            matrix[2][n - 2] -= factor * matrix[3][n - 3]
        elif i == n - 1:
            factor = matrix[0][n - 1] / matrix[1][n - 2]
            matrix[0][n - 1] = factor
            matrix[1][n - 1] -= factor * matrix[2][n - 2]
        else:
            factor = matrix[0][i] / matrix[1][i - 1]
            matrix[0][i] = factor
            matrix[1][i] -= factor * matrix[2][i - 1]
            matrix[2][i] -= factor * matrix[3][i - 1]

    # Aktualizacja wektora x
    for i in range(1, n):
        x[i] -= matrix[0][i] * x[i - 1]

    # Rozwiązanie dla wektora x
    x[n - 1] /= matrix[1][n - 1]
    x[n - 2] = (x[n - 2] - matrix[2][n - 2] * x[n - 1]) / matrix[1][n - 2]

    for i in reversed(range(n - 2)):
        x[i] = (x[i] - matrix[3][i] * x[i + 2] - matrix[2][i] * x[i + 1]) / matrix[1][i]

    # Obliczenie wyznacznika
    det = 1
    for diag_value in matrix[1]:
        det *= diag_value

    return x, det


N = 300
ex_time = []
s = list(range(5, N + 1))
res, determ = lufac(N)

print("Wynik:\n", res, "\n\nWyznacznik:\n", determ)


for value in s:
    start_time = time.time()
    lufac(value)
    ex_time.append(time.time() - start_time)


plt.figure(figsize=(20, 12))

plt.plot(s, ex_time,
         linestyle='-',
         color='green')

plt.title('Czas wykonania faktoryzacji w zależności od rozmiaru danych')
plt.xlabel('Rozmiar danych')
plt.ylabel('Czas wykonania (sekundy)')

plt.grid(visible=True)

plt.show()