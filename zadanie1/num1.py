import numpy as np
import matplotlib.pyplot as plt

x= np.float64(0.2)
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

def blad(f, x, h):
    return np.abs(f(x, h) - df(x))

def policz(x, hs64, hs32, wynik1, wynik2, wynik3, wynik4):

    for h in hs64:
        wynik1.append(blad(wzA, x, h))
        wynik2.append(blad(wzB, x, h))

    x = np.float32(x)
    for h in hs32:
        wynik3.append(blad(wzA, x, h))
        wynik4.append(blad(wzB, x, h))
    return

wynikA32 = []
wynikA64 = []
wynikB32 = []
wynikB64 = []

hs64 = np.logspace(-21,0,256,dtype=np.float64)
hs32 = np.logspace(-21,0,256,dtype=np.float32)

policz(x, hs64, hs32, wynikA64, wynikB64, wynikA32, wynikB32)

plt.figure(figsize=(19,11))
plt.loglog(hs32, wynikA32, label=f'Błąd forward difference float32')
plt.loglog(hs32, wynikB32, label=f'Błąd central difference float32', ls="-.")
plt.loglog(hs64, wynikA64, label=f'Błąd forward difference float64')
plt.loglog(hs64, wynikB64, label=f'Błąd central difference float64', ls="-.")
plt.xlabel('h')
plt.ylabel('|Dh_f(x) - f\'(x)|')
plt.title(f'Błąd w stosunku do h dla f(x) = sin(x^3), x = {x}')
plt.legend()
plt.grid(True)
plt.show()