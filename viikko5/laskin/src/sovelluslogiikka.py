class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.alku = None

    def miinus(self, arvo):
        self.tulos -= arvo

    def plus(self, arvo):
        self.tulos += arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def tallenna_alkutilanne(self):
        self.alku = self.tulos