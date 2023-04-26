from pathlib import Path

from player import Player
from hive import Hive
from game_over import GameOverScreen
from game_lib import Game, Screen, TextBox, LEFT, RIGHT, TOP, CENTERED

import pyxel as px


class RogersRevenge(Game):
    def __init__(self, fps):
        screen = Screen(320, 240)
        px.init(screen.width, screen.height,
                fps=fps, title="Roger's Revenge")
        self.version = Path("assets/version").read_text("utf-8")
        super().__init__("assets/resources.pyxres", fps,
                         screen)

    def setup(self):
        self.player = Player(self)
        Hive(self)
        score_box = TextBox(self, f"Score: {self.player.score}", 11)
        lives_box = TextBox(self, f"Lives: {self.player.lives}", 11)
        version_box = TextBox(self, self.version, 11)

        lives_box.place(LEFT, TOP)
        score_box.place(CENTERED, TOP)
        version_box.place(RIGHT, TOP)

        self.add_obj(lives_box)
        self.add_obj(score_box)
        self.add_obj(version_box)

    def increase_score(self, amount: int):
        self.player.score += amount

    def game_over(self):
        self.ticked_objs = []
        self.drawn_objects = []
        self.debug_objs = []
        GameOverScreen(self, self.player.score)


RogersRevenge(fps=30)
