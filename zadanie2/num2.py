import numpy as np

# Definiowanie macierzy A1 i A2
A1 = np.array([
    [5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064],
    [1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415],
    [0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230],
    [-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055],
    [0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879]
])

A2 = np.array([
    [5.4763986379, 1.6846933459, 0.3136661779, -1.0597154562, 0.0083249547],
    [1.6846933459, 4.6359087874, -0.6108766748, 2.1930659258, 0.9091647433],
    [0.3136661779, -0.6108766748, 1.4591897081, -1.1804364456, 0.3985316185],
    [-1.0597154562, 2.1930659258, -1.1804364456, 3.3110327980, -1.1617171573],
    [0.0083249547, 0.9091647433, 0.3985316185, -1.1617171573, 2.1174700695]
])

# Definiowanie wektora b
b = np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006])

# Rozwiązywanie układu równań A1 * y1 = b oraz A2 * y2 = b
y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)

# Wyświetlanie wyników
print("Rozwiązanie dla A1 * y1 = b:")
print(y1)

print("\nRozwiązanie dla A2 * y2 = b:")
print(y2)


# Wylosowanie wektora o losowych wartościach
n = len(b)  # rozmiar wektora
v = np.random.randn(n)  # generowanie wektora o rozmiarze n z rozkładem normalnym

# Obliczanie normy euklidesowej
norma_v = np.linalg.norm(v)

# Przeskalowanie wektora do normy około 10^-6
v_scaled = v * (1e-6 / norma_v)
# Wektor zaburzeń (b + Δb)
b_zaburzone = b + v_scaled
# Rozwiązywanie układów równań A1 * y1 = b + Δb oraz A2 * y2 = b + Δb
y1_zaburzone = np.linalg.solve(A1, b_zaburzone)
y2_zaburzone = np.linalg.solve(A2, b_zaburzone)

print("\n   Wektor zaburzeń (Δb):")
print(v_scaled)

print("\nWektor b + Δb:")
print(b_zaburzone)

print("\nRozwiązanie dla A1 * y1 = b + Δb:")
print(y1_zaburzone)

print("\nRozwiązanie dla A2 * y2 = b + Δb:")
print(y2_zaburzone, end="\n\n\n")



