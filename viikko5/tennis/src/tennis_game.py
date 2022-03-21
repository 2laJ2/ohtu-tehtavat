class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def deuce_score(self):
        if  self.player1_score == 0:
                return "Love-All"
        if  self.player1_score == 1:
                return "Fifteen-All"
        if  self.player1_score == 2:
                return "Thirty-All"
        if  self.player1_score == 3:
                return "Forty-All"
        return "Deuce"

    def advantage_score(self):
        difference = self.player1_score - self.player2_score
        if difference == 1:
            return "Advantage player1"
        if difference == -1:
            return "Advantage player2"
        if difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def player_score(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.deuce_score()
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.advantage_score()
        return f"{self.player_score(self.player1_score)}-{self.player_score(self.player2_score)}"
        
