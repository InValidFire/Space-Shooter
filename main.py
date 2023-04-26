from player import Player
from hive import Hive
from game_over import GameOverScreen
from lib import Game, Screen


class RogersRevenge(Game):
    def __init__(self):
        super().__init__("Roger's Revenge", "../resources.pyxres", 30,
                         Screen(320, 240))

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


RogersRevenge()
