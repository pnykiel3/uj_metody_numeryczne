import numpy as np
import matplotlib.pyplot as plt


class RozwiazywaczWlasnych:
    DOKLADNOSC = 1e-10
    MAKS_CYKLE = 1234

    def __init__(self, macierz):
        self.macierz = np.array(macierz)

    def metoda_potegowa(self):
        historia_wartosci = []
        historia_bledow = []

        def mnoz_macierz_wektor(macierz, wektor):
            return np.dot(macierz, wektor)

        def normalizuj(wektor):
            return wektor / np.linalg.norm(wektor)

        przypuszczenie = np.ones(len(self.macierz))
        przypuszczenie = normalizuj(przypuszczenie)

        poprzednia_wartosc_wlasna = 0
        for _ in range(RozwiazywaczWlasnych.MAKS_CYKLE):
            nastepne_przypuszczenie = mnoz_macierz_wektor(self.macierz, przypuszczenie)
            nastepne_przypuszczenie = normalizuj(nastepne_przypuszczenie)
            obecna_wartosc_wlasna = np.dot(nastepne_przypuszczenie, mnoz_macierz_wektor(self.macierz, nastepne_przypuszczenie))
            historia_wartosci.append(obecna_wartosc_wlasna)
            historia_bledow.append(abs(obecna_wartosc_wlasna - poprzednia_wartosc_wlasna))

            if historia_bledow[-1] < RozwiazywaczWlasnych.DOKLADNOSC:
                break

            przypuszczenie = nastepne_przypuszczenie
            poprzednia_wartosc_wlasna = obecna_wartosc_wlasna

        return historia_bledow, historia_wartosci, przypuszczenie

    def metoda_qr(self):
        aktualna_macierz = self.macierz.copy()
        licznik_iteracji = 0

        slady_diagonalne = [[] for _ in range(len(aktualna_macierz))]
        slady_poddiagonalne = [[] for _ in range(len(aktualna_macierz) - 1)]
        slady_odchylen = [[] for _ in range(len(aktualna_macierz))]

        rzeczywiste_wartosci = np.linalg.eigvals(self.macierz)

        while licznik_iteracji < RozwiazywaczWlasnych.MAKS_CYKLE:
            Q, R = np.linalg.qr(aktualna_macierz)
            aktualna_macierz = R @ Q

            for i in range(len(aktualna_macierz)):
                slady_diagonalne[i].append(aktualna_macierz[i, i])
                slady_odchylen[i].append(abs(aktualna_macierz[i, i] - rzeczywiste_wartosci[i]))

            for i in range(len(aktualna_macierz) - 1):
                slady_poddiagonalne[i].append(abs(aktualna_macierz[i + 1, i]))

            maks_poddiagonalna = max(abs(aktualna_macierz[i + 1, i]) for i in range(len(aktualna_macierz) - 1))
            if maks_poddiagonalna < RozwiazywaczWlasnych.DOKLADNOSC:
                break

            licznik_iteracji += 1

        return slady_diagonalne, slady_poddiagonalne, slady_odchylen

    def wizualizuj_metode_potegowa(self):
        bledy, wartosci_wlasne, wektor_wlasny = self.metoda_potegowa()

        plt.figure(figsize=(8, 6))
        plt.semilogy(bledy, marker='D', color='red', label="Błąd w kolejnych iteracjach")
        plt.title("Zbieżność metody potęgowej")
        plt.xlabel("Iteracje")
        plt.ylabel("Błąd")
        plt.legend()
        plt.grid(True)
        plt.show()

        print("Największa wartość własna:", wartosci_wlasne[-1])
        print("Obliczony wektor własny:", wektor_wlasny)

    def wizualizuj_metode_qr(self):
        slady_diag, slady_poddiag, odchylenia = self.metoda_qr()

        plt.figure(figsize=(11, 7))
        for idx, odch in enumerate(odchylenia):
            plt.semilogy(range(len(odch)), odch, label=f"Element diagonalny {idx + 1}")
        plt.title("Odchylenia elementów diagonalnych")
        plt.xlabel("Iteracje")
        plt.ylabel("Odchylenie")
        plt.legend()
        plt.grid(True)
        plt.show()

        plt.figure(figsize=(11, 7))
        for idx, pododch in enumerate(slady_poddiag):
            plt.semilogy(range(len(pododch)), pododch, label=f"Element poddiagonalny {idx + 1}")
        plt.title("Zbieżność elementów poddiagonalnych")
        plt.xlabel("Iteracje")
        plt.ylabel("Wartość")
        plt.legend()
        plt.grid(True)
        plt.show()

        koncowe_wartosci_wlasne = [float(diag[-1]) for diag in slady_diag]
        print("Wartości własne:", koncowe_wartosci_wlasne)

    def uruchom_wszystkie_metody(self):
        print("\t\tMETODA POTEGOWA")
        self.wizualizuj_metode_potegowa()

        print("\t\tMETODA QR")
        self.wizualizuj_metode_qr()


dane_wejsciowe = [
    [9, 2, 0, 0],
    [2, 4, 1, 0],
    [0, 1, 3, 1],
    [0, 0, 1, 2]
]

instancja_rozwiazywacza = RozwiazywaczWlasnych(dane_wejsciowe)
instancja_rozwiazywacza.uruchom_wszystkie_metody()

wartosci_numpy = np.linalg.eigvals(dane_wejsciowe)
print("\t\tNUMPY")
print("Wartości własne:", wartosci_numpy)
