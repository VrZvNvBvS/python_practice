class Player:

    def __init__(self, player):
        print(player)
        self.name = player['name']
        self.age = player['age']
        self.position = ['position']
        self.team = player['team']

    def shoot(self):
        print(f"{self.name} shoots the ball.")

    @classmethod
    def get_team(cls, team_list):
        new_player_list = []
        for player in team_list:
            new_player_list.append(Player(player))
        return new_player_list
