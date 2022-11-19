import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games'],
            )

            self.players.append(player)

    def __str__(self):
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.list = reader
        self.list.sort(key=lambda h: (h.pisteet), reverse=True)
    
    def top_scorers_by_nationality(self, nation):
        self.new_list = []
        for player in self.list:
            if player['nationality'] == nation:
                self.new_list.append(player)
        return self.new_list

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
