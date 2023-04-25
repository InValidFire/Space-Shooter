from lib import Vector, GameObject, Box


class Missile(GameObject):
    def __init__(self, game, direction: Vector, pos: Vector, color: int):
        super().__init__(game)
        self.shape = Box(2, 4)
        self.direction = direction
        self.pos = pos
        self.color = color
        self.game.add_obj(self, True)
        self.tick_task(self.move)

    def draw(self):
        self.shape.draw(self.color)

    def move(self):
        speed_multiplier = 160  # pixels/sec
        self.speed = self.direction.normalize() * speed_multiplier
        self.pos += self.speed * self.game.delta_time
        if not self.game.screen.is_touching(self.shape):
            self.game.remove_obj(self)

    def __repr__(self) -> str:
        return f"Missile:{self.pos}"
