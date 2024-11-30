KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        for alkio in range(0, self.alkioiden_lkm):
            if numero == self.lukujono[alkio]:
                return True
        return False

    def lisaa(self, numero):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = numero
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(numero):
            self.lukujono[self.alkioiden_lkm] = numero
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lukujono) == 0:
                self.luo_uusi_sailytyspaikka()

            return True

        return False

    def luo_uusi_sailytyspaikka(self):
        taulukko_old = self.lukujono
        self.kopioi_lista(self.lukujono, taulukko_old)
        self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.lukujono)

    def poista(self, numero):
        kohta = -1
        apu = 0

        for alkio in range(0, self.alkioiden_lkm):
            if numero == self.lukujono[alkio]:
                kohta = alkio  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            self.siirra_alkio_loppuun(kohta)

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def siirra_alkio_loppuun(self, kohta):
        for alkio in range(kohta, self.alkioiden_lkm - 1):
            apu = self.lukujono[alkio]
            self.lukujono[alkio] = self.lukujono[alkio + 1]
            self.lukujono[alkio + 1] = apu

    def kopioi_lista(self, lista_a, lista_b):
        for alkio in range(0, len(lista_a)):
            lista_b[alkio] = lista_a[alkio]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for alkio in range(0, len(taulu)):
            taulu[alkio] = self.lukujono[alkio]

        return taulu

    @staticmethod
    def yhdiste(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.to_int_list()
        b_taulu = lista_b.to_int_list()

        for alkio in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[alkio])

        for alkio in range(0, len(b_taulu)):
            joukko.lisaa(b_taulu[alkio])

        return joukko

    @staticmethod
    def leikkaus(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.to_int_list()
        b_taulu = lista_b.to_int_list()

        for alkio_a in range(0, len(a_taulu)):
            for alkio_b in range(0, len(b_taulu)):
                if a_taulu[alkio_a] == b_taulu[alkio_b]:
                    joukko.lisaa(b_taulu[alkio_b])

        return joukko

    @staticmethod
    def erotus(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.to_int_list()
        b_taulu = lista_b.to_int_list()

        for alkio in range(0, len(a_taulu)):
            joukko.lisaa(a_taulu[alkio])

        for alkio in range(0, len(b_taulu)):
            joukko.poista(b_taulu[alkio])

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for alkio in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[alkio])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
