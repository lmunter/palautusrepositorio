import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:5} {self.goals} + {self.assists} = {self.points}"

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = []
        for player in self.reader:
            if player.nationality == nationality:
                filtered_players.append(player)
        sorted_players = sorted(filtered_players, key=lambda x: x.points, reverse=True)
        return sorted_players

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        player_dict = requests.get(self.url).json()
        player_list = []
        for player in player_dict:
            player_list.append(Player(player))
        return player_list
