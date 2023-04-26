import random as r
from lib import Vector, GameObject, Box, IS_TOUCHED
from missile import Missile

from balance import Balance


class Enemy(GameObject):
    def __init__(self, game, pos: Vector):
        super().__init__(game)
        self.shape = Box(Balance.enemy_width, Balance.enemy_height)
        self.speed = Balance.enemy_speed
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
                self.game.increase_score(Balance.enemy_score)
                self.game.remove_obj(self)

    def attack_player(self):
        if not self.can_attack or (self.game.time - self.last_shot_sec) <= 1:
            return
        chance = r.randrange(Balance.enemy_fire_chance[0],
                             Balance.enemy_fire_chance[1])
        if self.pos.x <= self.game.player.pos.x + (Balance.player_width * 2) and self.pos.x >= self.game.player.pos.x - Balance.player_width:
            if chance <= int(Balance.enemy_fire_chance[1]/5):
                Missile(self.game, Vector(0, 1),
                        Vector(self.pos.x, self.pos.y + self.shape.height + 2), 10)
                self.last_shot_sec = self.game.time
        else:
            if chance == 1:
                Missile(self.game, Vector(0, 1),
                        Vector(self.pos.x, self.pos.y + self.shape.height + 2), 10)

    def draw(self):
        self.shape.draw(10)
