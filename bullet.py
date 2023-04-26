import pyxel as px
from game_lib import Vector, GameObject, Box


class Bullet(GameObject):
    def __init__(self, game, direction: Vector, pos: Vector):
        super().__init__(game)
        self.shape = Box(4, 5, 4)
        self.direction = direction
        self.pos = pos
        self.game.add_obj(self, True)
        self.tick_task(self.move)

    def draw(self):
        px.blt(self.pos.x, self.pos.y, 0, 16, 0, 5, 5, 0)

    def move(self):
        speed_multiplier = 196  # pixels/sec
        self.speed = self.direction.normalize() * speed_multiplier
        self.pos += self.speed * self.game.delta_time
        if not self.game.screen.is_touching(self.shape):
            self.game.remove_obj(self)

    def __repr__(self) -> str:
        return f"Missile:{self.pos}"
