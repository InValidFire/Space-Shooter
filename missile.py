from lib import Vector, GameObject, Box
from enemy import Enemy


class Missile(GameObject):
    def __init__(self, game, velocity: Vector, pos: Vector):
        super().__init__(game)
        self.shape = Box(4, 12)
        self.velocity = velocity
        self.pos = pos
        self.game.add_obj(self, True)

    def draw(self):
        self.shape.draw(11)

    def update(self):
        self._collision_objs = []
        for obj in self.game.game_objs:
            if isinstance(obj, Enemy):
                self.add_collision_check(obj, 0)
        velocity_multiplier = 128
        self.velocity = self.velocity.normalize() * velocity_multiplier
        self.pos += self.velocity * self.game.delta_time
        for collision_obj in self.check_collisions():
            self.game.remove_obj(collision_obj)
            self.game.remove_obj(self)
        if not self.game.screen.is_touching(self.shape):
            self.game.remove_obj(self)

    def __repr__(self) -> str:
        return f"Missile:{self.pos}"
