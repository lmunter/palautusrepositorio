class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
