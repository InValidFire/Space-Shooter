import pyxel as px

from lib import Vector, GameObject, Box
from missile import Missile


class Player(GameObject):
    def __init__(self, game):
        super().__init__(game)
        self.shape = Box(16, 16)
        self.pos = self.game.screen.scaled_pos(.5, .9)  # x, y
        self.last_shot_sec = -2
        self.speed = Vector(0, 0)  # x, y
        self._color = 11
        self.lives = 3
        self.game.add_obj(self, True)
        self.tick_task(self.move)
        self.tick_task(self.shoot_missile)

    def move(self):
        speed_multiplier = 128  # pixels/second
        screen_width = self.game.screen.width
        screen_height = self.game.screen.height

        self.speed = Vector(0, 0)

        if px.btn(px.KEY_LEFT):
            self.speed.x -= 1
        if px.btn(px.KEY_RIGHT):
            self.speed.x += 1

        self.speed = self.speed.normalize() * speed_multiplier
        self.pos += self.speed * self.game.delta_time

        # ensure player doesn't leave the play area
        self.pos = self.pos.clamp_x(0, screen_width - self.shape.width)
        self.pos = self.pos.clamp_y(0, screen_height - self.shape.height)

    def shoot_missile(self):
        if px.btnp(px.KEY_UP) and (self.game.time - self.last_shot_sec) > 1:
            self.last_shot_sec = self.game.time
            Missile(self.game, Vector(0, -1),
                    Vector(self.pos.x + (self.shape.width/4),
                           self.pos.y - (self.shape.height + 2)))

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
