import numpy as np
import matplotlib.pyplot as plt
import random
import copy


def jacobi(x, stop, d):
    if d == 0:
        raise ValueError("d cannot be 0")
    error = []
    nrm0 = 0

    while stop:
        y = x.copy()
        for i in range(n):
            match i:
                case 0:
                    x[i] = (b[i] - 0.5 * x[i + 1] - 0.1 * x[i + 2]) / d
                case 1:
                    x[i] = (b[i] - 0.5 * y[i - 1] - 0.5 * x[i + 1] - 0.1 * x[i + 2]) / d
                case _ if i == n - 2:
                    x[i] = (b[i] - 0.5 * y[i - 1] - 0.1 * y[i - 2] - 0.5 * x[i + 1]) / d
                case _ if i == n - 1:
                    x[i] = (b[i] - 0.5 * y[i - 1] - 0.1 * y[i - 2]) / d
                case _:
                    x[i] = (b[i] - 0.5 * y[i - 1] - 0.1 * y[i - 2] - 0.5 * x[i + 1] - 0.1 * x[i + 2]) / d

        nrm1 = np.sqrt(sum((a0 - a1) ** 2 for a0, a1 in zip(x, y)))
        error.append(copy.deepcopy(x))

        # Sprawdzenie czy zbiegło
        if abs(nrm0 - nrm1) < 10 ** (-13):
            break
        nrm0 = nrm1
        stop -= 1

    return error


def gauss(x, stop, d):
    if d == 0:
        raise ValueError("d cannot be 0")
    error = []
    nrm0 = 0

    while stop:
        y = x.copy()
        for i in range(n):
            match i:
                case 0:
                    x[i] = (b[i] - 0.5 * x[i + 1] - 0.1 * x[i + 2]) / d
                case 1:
                    x[i] = (b[i] - 0.5 * x[i - 1] - 0.5 * x[i + 1] - 0.1 * x[i + 2]) / d
                case _ if i == n - 2:
                    x[i] = (b[i] - 0.5 * x[i - 1] - 0.1 * x[i - 2] - 0.5 * x[i + 1]) / d
                case _ if i == n - 1:
                    x[i] = (b[i] - 0.5 * x[i - 1] - 0.1 * x[i - 2]) / d
                case _:
                    x[i] = (b[i] - 0.5 * x[i - 1] - 0.1 * x[i - 2] - 0.5 * x[i + 1] - 0.1 * x[i + 2]) / d

        nrm1 = np.sqrt(sum((a0 - a1) ** 2 for a0, a1 in zip(x, y)))
        error.append(copy.deepcopy(x))

        # Sprawdzenie czy zbiegło
        if abs(nrm0 - nrm1) < 10 ** (-13):
            break
        nrm0 = nrm1
        stop -= 1

    return error


# Parametry
d_values = [ 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.3, 1.35, 1.4, 1.5, 1.7, 2]
n = 200
stop = 500
b = list(range(1, n + 1))

# Tworzenie wykresu
plt.figure(figsize=(12, 8))
plt.grid(True)
plt.xlabel('n')
plt.ylabel("$|x(n) - x(ostatni)|$")
plt.yscale('log')
plt.title('Porównanie metod iteracyjnych dla różnych wartości d')

# Dla każdej wartości d wykonujemy iteracje metodą Jacobiego i Gaussa-Seidela
for d in d_values:
    x = random.sample(range(500), n)  # losowy wektor startowy dla każdej wartości d

    err1 = jacobi(x.copy(), stop, d)
    err2 = gauss(x.copy(), stop, d)

    # Obliczanie różnicy pomiędzy rozwiązaniem w poszczególnych iteracjach a rozwiązaniem dokładnym
    w1 = []
    last1 = err1[-1]
    for i in range(len(err1) - 1):
        w1.append(np.sqrt(sum((a0 - a1) ** 2 for a0, a1 in zip(err1[i], last1))))

    w2 = []
    last2 = err2[-1]
    for i in range(len(err2) - 1):
        w2.append(np.sqrt(sum((a0 - a1) ** 2 for a0, a1 in zip(err2[i], last2))))

    # Dodajemy wyniki dla bieżącej wartości d na wykresie
    plt.plot(range(1, len(w1) + 1), w1, label=f'Jacobi, d = {d}')
    plt.plot(range(1, len(w2) + 1), w2, linestyle='--', label=f'Gauss-Seidel, d = {d}')

# Dodanie legendy
plt.legend()
plt.show()
