import numpy as np
import matplotlib.pyplot as plt

# double czyli float 64 -16 do 0
# float -7 do 0

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

def liczenie(x, hs):
    wynikA = []
    wynikB = []

    for h in hs:
        #błąd to bezwzględna różnica wartości przybliżonej od wartości dokładnej
        bladA = np.abs(wzA(x, h) - df(x))
        bladB = np.abs(wzB(x, h) - df(x))

        wynikA.append(bladA)
        wynikB.append(bladB)

    return wynikA, wynikB

# punkt do badania pochodnej
x = 0.2

hs64 = np.logspace(-16, 0, 256)
#hs32 = np.logspace(-7, 0, 128)
hs32 = hs64.astype(np.float32)
bladA32, bladB32 = liczenie(x, hs32)
bladA64, bladB64 = liczenie(x, hs64)

    # wykres błędów
plt.figure(figsize=(13,7))
plt.loglog(hs32, bladA32, label=f'Błąd (a) float32')
plt.loglog(hs32, bladB32, label=f'Błąd (b) float32')
plt.xlabel('h')
plt.ylabel('|Dh_f(x) - f\'(x)|')
plt.title(f'Błąd w stosunku do h dla f(x) = sin(x^3), x = {x}')
plt.legend()
plt.grid()

plt.figure(figsize=(13,7))
plt.loglog(hs64, bladA64, label=f'Błąd (a) float64')
plt.loglog(hs64, bladB64, label=f'Błąd (b) float64')
plt.xlabel('h')
plt.ylabel('|Dh_f(x) - f\'(x)|')
plt.title(f'Błąd w stosunku do h dla f(x) = sin(x^3), x = {x}')
plt.legend()
plt.grid(True, which="both", ls = "--")
plt.show()
