import pyxel as px

from game_lib import Vector, GameObject, Box, IS_TOUCHED
from bullet import Bullet


class Player(GameObject):
    fire_delay = 1
    width = 16
    height = 16
    speed_multiplier = 96

    def __init__(self, game):
        super().__init__(game)
        self.shape = Box(Player.width, Player.height, 2)
        self.pos = self.game.screen.scaled_pos(.5, .9)  # x, y
        self.last_shot_sec = -2
        self.speed = Vector(0, 0)  # x, y
        self.score = 0
        self.lives = 2
        self.immortal = False
        self.game.add_obj(self, True)
        self.add_collision_check(Bullet, IS_TOUCHED)
        self.tick_task(self.check_collisions)
        self.tick_task(self.die)
        self.tick_task(self.move)
        self.tick_task(self.shoot_bullet)

    def get_attack_radius(self):
        return self.pos.x - self.shape.width, self.pos.x + self.shape.width * 2

    def die(self):
        if self.immortal:
            return
        for collision_obj in self.collisions:
            if isinstance(collision_obj, Bullet):
                self.lives -= 1
                px.play(0, 0)
                self.game.remove_obj(collision_obj)
            if self.lives < 0:
                self.game.game_over()

    def move(self):
        speed_multiplier = Player.speed_multiplier  # pixels/second
        screen_width = self.game.screen.width
        screen_height = self.game.screen.height

        self.speed = Vector(0, 0)

        if px.btn(px.KEY_LEFT):
            self.speed.x -= 1
        if px.btn(px.KEY_RIGHT):
            self.speed.x += 1
        if px.btnp(px.KEY_F8):
            self.immortal = not self.immortal

        self.speed = self.speed.normalize() * speed_multiplier
        self.pos += self.speed * self.game.delta_time

        # ensure player doesn't leave the play area
        self.pos = self.pos.clamp_x(0, screen_width - self.shape.width)
        self.pos = self.pos.clamp_y(0, screen_height - self.shape.height)

    def shoot_bullet(self):
        can_shoot = (self.game.time - self.last_shot_sec) > Player.fire_delay
        if px.btnp(px.KEY_UP) and can_shoot:
            self.last_shot_sec = self.game.time
            Bullet(self.game, Vector(0, -1),
                   Vector(self.pos.x + (self.shape.width/4) + 4,
                          self.pos.y - 2))

    def draw(self):
        px.blt(self.pos.x, self.pos.y, 0, 0, 0, 16, 16, 0)
