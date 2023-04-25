from player import Player
from enemy import Enemy
from lib import Game


class RevengeOfRoger(Game):
    def setup(self):
        Player(self)
        Enemy.setup(self)


RevengeOfRoger()
