class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def deuce_score(self):
        if  self.m_score1 == 0:
                return "Love-All"
        if  self.m_score1 == 1:
                return "Fifteen-All"
        if  self.m_score1 == 2:
                return "Thirty-All"
        if  self.m_score1 == 3:
                return "Forty-All"
        return "Deuce"

    def advantage_score(self):
        difference = self.m_score1 - self. m_score2

        if difference == 1:
            return "Advantage player1"
        if difference == -1:
            return "Advantage player2"
        if difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def player_score(self, temp_score):
        if temp_score == 0:
            return "Love"
        if temp_score == 1:
            return "Fifteen"
        if temp_score == 2:
            return "Thirty"
        if temp_score == 3:
            return "Forty"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.deuce_score()
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.advantage_score()
        
        #score = ""
        for i in range(1, 3):
            return f"{self.player_score(self.m_score1)}-{self.player_score(self.m_score2)}"
            #if i == 1:
            #    score += self.player_score(self.m_score1)
            #else:
            #    score += "-"+self.player_score(self.m_score2)
            
        #return score
