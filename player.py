import pyxel as py

from lib import Vector, GameObject, Box
from missile import Missile


class Player(GameObject):
    def __init__(self, game):
        super().__init__(game)
        self.shape = Box(16, 16)
        self.pos = self.game.screen.scaled_pos(.5, .9)  # x, y
        self.speed = Vector(0, 0)  # x, y
        self._color = 11
        self.health = 100

    def update(self):
        speed_multiplier = 128  # pixels/second
        screen_width = self.game.screen.width
        screen_height = self.game.screen.height

        self.speed = Vector(0, 0)

        if py.btn(py.KEY_LEFT):
            self.speed.x -= 1
        if py.btn(py.KEY_RIGHT):
            self.speed.x += 1
        if py.btnp(py.KEY_UP):
            Missile(self.game, Vector(0, -1),
                    Vector(self.pos.x + (self.shape.width/4),
                           self.pos.y - (self.shape.height + 2)))
        self.speed = self.speed.normalize() * speed_multiplier
        self.pos += self.speed * self.game.delta_time

        # ensure player doesn't leave the play area
        self.pos = self.pos.clamp_x(0, screen_width - self.shape.width)
        self.pos = self.pos.clamp_y(0, screen_height - self.shape.height)

    def draw(self):
        self.shape.draw(11)

    @property
    def color(self) -> int:
        return self._color

    @color.setter
    def color(self, value: int):
        if type(value) != int:
            raise TypeError(value)
        else:
            self._color = value
