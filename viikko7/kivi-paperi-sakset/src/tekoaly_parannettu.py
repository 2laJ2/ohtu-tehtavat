# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = []
        self._muistin_koko = muistin_koko

    def aseta_siirto(self, siirto):
        self._muisti.append(siirto)
        if len(self._muisti) > self._muistin_koko:
            self._muisti.pop()
        # jos muisti täyttyy, unohdetaan viimeinen alkio

    def anna_siirto(self):
        if len(self._muisti) < 2:
            return "k"

        viimeisin_siirto = self._muisti[- 1]

        k = 0
        p = 0
        s = 0

        for i in range(0, len(self._muisti) - 2):
            if viimeisin_siirto == self._muisti[i]:
                seuraava_siirto = self._muisti[i + 1]

                if seuraava_siirto == "k":
                    k += 1
                elif seuraava_siirto == "p":
                    p += 1
                else:
                    s += 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return "p"
        elif p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
