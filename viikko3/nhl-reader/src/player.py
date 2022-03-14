import re
import requests

class Player:

    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.score = self.goals + self.assists
        
    def __str__(self):
        playerInfo = f"{str(self.name):30} {str(self.team):5} {str(self.goals):2} + {str(self.assists):2} = {str(self.score):2}"
        return playerInfo
