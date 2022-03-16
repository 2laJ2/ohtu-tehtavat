from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self.ostoskori:
            lukumaara += ostos.lukumaara()

        return lukumaara

    def hinta(self):
        summa = 0
        for ostos in self.ostoskori:
            summa += ostos.lukumaara() * ostos.tuote.hinta()
        
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuote.nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuote.nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostoskori.remove(ostos)

    def tyhjenna(self):
        self.ostoskori = []

    def ostokset(self):
        tuotteet = []
        for ostos in self.ostoskori:
            tuotteet.append(ostos)
        return tuotteet
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
