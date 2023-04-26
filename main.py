from pathlib import Path

from player import Player
from hive import Hive
from hud import HUD
from game_lib import Game, Screen

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
        self.debug_objs = []
        self.ticked_objs = []
        self.drawn_objects = []
        self.player = Player(self)
        Hive(self)
        self.hud = HUD(self)

    def increase_score(self, amount: int):
        self.player.score += amount


RogersRevenge(fps=30)
