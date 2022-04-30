from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps import KPS
from kps_peli import KPSpeli


class Konsoli():

    def __init__(self):
        self._peli = KPSpeli()
        self._pelivalinta = {
                "a" : self._peli.kps_pelaaja_vs_pelaaja(),
                "b" : self._peli.kps_tekoaly(),
                "c" : self._peli.kps_parempi_tekoaly()
            }

    def _valitse_peli(self, vastaus):
        self._pelivalinta[vastaus].pelaa()

    def _valikko(self):
        while True:
            print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )

            vastaus = input()

            if vastaus in "abc":
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )
                self._valitse_peli(vastaus[len(vastaus)-1])

            else:
                break