class Player:
    def __init__(self, name, nation, assists, goals, penalties, team, games):
        self.name = name
        self.nation = nation
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.pisteet = assists+goals
    
    def __str__(self):
        return f"{self.name:20} pisteet: {self.pisteet}"
