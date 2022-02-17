import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub()
        )

    def test_etsi_pelaaja_nimella(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(str(player),"Semenko EDM 4 + 12 = 16") 

    def test_pelaaja_ei_loydy_nimella(self):
        player = self.statistics.search("Selanne")
        self.assertEqual(player,None)       

    def test_etsi_joukkue(self):
        team = self.statistics.team("DET")
        self.assertEqual(team,[self.statistics.search("Yzerman")])

    def test_joukkuetta_ei_loydy_nimella(self):
        team = self.statistics.team("DREAM TEAM")
        self.assertEqual(team,[])  

    def test_etsi_parhaat_pelaajat(self):
        players = self.statistics.top_scorers(0)
        self.assertEqual(players,[self.statistics.search("Gretzky")])