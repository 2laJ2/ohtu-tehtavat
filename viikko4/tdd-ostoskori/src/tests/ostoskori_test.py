from optparse import make_option
import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):

    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("mehu", 3))

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("mehu", 3))

        self.assertEqual(self.kori.hinta(), 8)


    def test__kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("maito", 5))

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test__kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("maito", 5))

        self.assertEqual(self.kori.hinta(), 10)

    def test_yhden_tuotteen_lisaamisen_jalkseen_korissa_yksi_ostosolio(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(len(self.kori.ostokset()), 1)        

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        mehu = Tuote("Mehu", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lukumaara_2(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "maito")
        self.assertEqual(ostos.lukumaara(), 2) 

    def test_jos_korissa_on_kaksi_samaa_tuoteta_ja_toinen_naista_poistetaan_jaa_koriin_ostos_jossa_on_tuotetta_1_kpl(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.lukumaara(), 1)

    def test_koriin_lisatty_tuote_poistetaan_kori_on_taman_jalkeen_tyhja(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostoskori) == 0, True)

    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
 
    def test_lisaa_kaksi_samaa_ja_yksi_eri_tuote_ostoskoriin_tavaroiden_lukumaara_on_oikea(self):#
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("mehu", 3))

        self.assertEqual(self.kori.tavaroita_korissa(), 3)

    def test_lisaa_kaksi_samaa_ja_yksi_eri_tuote_ostoskoriin_ostoskori_laskee_oikein_tuotteiden_yhteenlasketun_hinnan(self):
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("maito", 5))
        self.kori.lisaa_tuote(Tuote("mehu", 3))

        self.assertEqual(self.kori.hinta(), 13)

    
    def test_lisaa_kaksi_samaa_ja_yksi_eri_tuote_ostoskoriin_poista_tuote_ostoskorista_ostoskori_laskee_oikein_tuotteiden_yhteenlasketun_hinnan(self):
        maito = Tuote("maito", 5)
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        self.kori.poista_tuote(maito)

        self.assertEqual(self.kori.hinta(), 8)

    def test_lisaa_kaksi_samaa_ja_yksi_eri_tuote_ostoskoriin_ostoskori_palauttaa_ostokset_listana_oikein(self):
        maito = Tuote("maito", 5)
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(mehu)
        tuotekori = self.kori.ostoskori
        self.assertEqual(len(self.kori.ostoskori) == 2, True)
        self.assertEqual(self.kori.ostokset(), tuotekori)