import random as r
from game_lib import Vector, GameObject, Box, IS_TOUCHED
from bullet import Bullet


class Enemy(GameObject):
    width = 16
    height = 16
    speed_multiplier = 30
    score = 100
    fire_chance = (1, 1000)

    def __init__(self, game, pos: Vector):
        super().__init__(game)
        self.shape = Box(Enemy.width, Enemy.height)
        self.speed = Enemy.speed_multiplier
        self.last_shot_sec = -2
        self.can_attack = False
        self.pos = pos
        self.game.add_obj(self, True)
        self.add_collision_check(Bullet, IS_TOUCHED)
        self.tick_task(self.check_collisions)
        self.tick_task(self.attack_player)
        self.tick_task(self.die)

    def die(self):
        for collision_obj in self.collisions:
            if isinstance(collision_obj, Bullet):
                self.game.remove_obj(collision_obj)
                self.game.increase_score(Enemy.score)
                self.game.remove_obj(self)

    def attack_player(self):
        if not self.can_attack or (self.game.time - self.last_shot_sec) <= 1:
            return
        chance = r.randrange(Enemy.fire_chance[0],
                             Enemy.fire_chance[1])
        attack_range = self.game.player.get_attack_radius()
        if self.pos.x <= attack_range[1] and self.pos.x >= attack_range[0]:
            if chance <= int(Enemy.fire_chance[1]/5):
                Bullet(self.game, Vector(0, 1),
                       Vector(self.pos.x, self.pos.y + self.shape.height + 2))
                self.last_shot_sec = self.game.time
        else:
            if chance == 1:
                Bullet(self.game, Vector(0, 1),
                       Vector(self.pos.x, self.pos.y + self.shape.height + 2))

    def draw(self):
        self.shape.draw(10)
