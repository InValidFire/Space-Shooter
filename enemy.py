import random as r
from lib import Vector, GameObject, Box, IS_TOUCHED
from missile import Missile


class Enemy(GameObject):
    def __init__(self, game, pos: Vector, size: int):
        super().__init__(game)
        self.shape = Box(self.game.screen.scaled_height(size), size)
        self.speed = 60
        self.last_shot_sec = -2
        self.can_attack = False
        self.pos = pos
        self.game.add_obj(self, True)
        self.add_collision_check(Missile, IS_TOUCHED)
        self.tick_task(self.check_collisions)
        self.tick_task(self.attack_player)
        self.tick_task(self.die)

    def die(self):
        for collision_obj in self.collisions:
            if isinstance(collision_obj, Missile):
                self.game.remove_obj(collision_obj)
                self.game.increase_score(100)
                self.game.remove_obj(self)

    def attack_player(self):
        if not self.can_attack or (self.game.time - self.last_shot_sec) <= 1:
            return
        chance = r.randrange(1, 200)
        if chance == 1:
            Missile(self.game, Vector(0, 1),
                    Vector(self.pos.x, self.pos.y + self.shape.height + 2), 10)
            self.last_shot_sec = self.game.time

    def draw(self):
        self.shape.draw(10)
