import numpy as np
import matplotlib.pyplot as plt

# f(x) = sin(x^3)
def f(x):
    return np.sin(x**3)

# pochodna
def df(x):
    return 3*x**2*np.cos(x**3)

# wzór z pkt. a
def wzA(x, h):
    return (f(x + h) - f(x)) / h

# wzór z pkt. b
def wzB(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# wzór na błąd
def blad(przyblizona, dokladna):
    return np.abs(przyblizona - dokladna)

# funkcja rysująca wykres błędów
def wykres(x, hs, dtype=np.float32):

    # konwersja dla zmiennoprzecinkowych
    hs = hs.astype(dtype)

    dokladna = df(x)

    wynikA = []
    wynikB = []

    for h in hs:
        dfA = wzA(x, h)
        dfB = wzB(x, h)

        bladA = blad(dfA, dokladna)
        bladB = blad(dfB, dokladna)

        wynikA.append(bladA)
        wynikB.append(bladB)

    # wykres błędów
    plt.figure(figsize=(12.8,7.2))
    plt.loglog(hs, wynikA, label=f'Błąd (a), dtype={dtype.__name__}', marker='o')
    plt.loglog(hs, wynikB, label=f'Błąd (b), dtype={dtype.__name__}', marker='x')

    plt.xlabel('h')
    plt.ylabel('|Dh_f(x) - f\'(x)|')
    plt.title(f'Błąd w stosunku do h dla f(x) = sin(x^3), x = {x}')
    plt.legend()
    plt.grid(True, which="both", ls = "--")
    plt.show()

# test dla różnych wartości h i typów zmiennoprzecinkowych
hs = np.logspace(-16, 0, 100)

# punkt do badania pochodnej
x = 0.2

# wykres dla float32
wykres(x, hs, dtype=np.float32)

# wykres dla float64
wykres(x, hs, dtype=np.float64)