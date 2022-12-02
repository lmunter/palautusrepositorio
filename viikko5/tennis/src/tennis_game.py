class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score = ""

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            self.get_even_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            self.check_for_win()
        else:
            self.get_player1_score()
            self.get_player2_score()
        return self.score

    def get_player1_score(self):
        if self.m_score1 == 0:
            self.score = "Love-"
        elif self.m_score1 == 1:
            self.score = "Fifteen-"
        elif self.m_score1 == 2:
            self.score = "Thirty-"
        elif self.m_score1 == 3:
            self.score = "Forty-"
        return self.score
    
    def get_player2_score(self):
        if self.m_score2 == 0:
            self.score = self.score + "Love"
        elif self.m_score2 == 1:
            self.score = self.score + "Fifteen"
        elif self.m_score2 == 2:
            self.score = self.score + "Thirty"
        elif self.m_score2 == 3:
            self.score = self.score + "Forty"
        return self.score
    
    def get_even_score(self):
        if self.m_score1 == 0:
            self.score = "Love-All"
        elif self.m_score1 == 1:
            self.score = "Fifteen-All"
        elif self.m_score1 == 2:
            self.score = "Thirty-All"
        elif self.m_score1 == 3:
            self.score = "Forty-All"
        else:
            self.score = "Deuce"
        return self.score
    
    def check_for_win(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"
        return self.score