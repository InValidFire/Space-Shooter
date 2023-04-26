from player import Player
from hive import Hive
from game_over import GameOverScreen
from lib import Game


class RevengeOfRoger(Game):
    def setup(self):
        self.player = Player(self)
        Hive(self)

    def increase_score(self, amount: int):
        self.player.score += amount

    def game_over(self):
        self.ticked_objs = []
        self.drawn_objects = []
        self.debug_objs = []
        GameOverScreen(self, self.player.score)


RevengeOfRoger("../resources.pyxres", 30)
