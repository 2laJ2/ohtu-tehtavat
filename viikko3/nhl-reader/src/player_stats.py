from player import Player
from player_reader import PlayerReader

class PlayerStats():

    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_list = []
        
        for p in self.players:
            if p.nationality == nationality:
                nationality_list.append(p)
            
        nationality_list.sort(key = lambda pl: pl.score, reverse = True)

        return nationality_list