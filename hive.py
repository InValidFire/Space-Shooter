import pyxel as px
from game_lib import GameObject, Game, Box, Vector
from enemy import Enemy


def get_spread_spacing(width_of_n, n, length):
    return (length - width_of_n)/(n-1) - width_of_n


class Hive(GameObject):
    def __init__(self, game: Game, enemy_cols: int = 10,
                 enemy_rows: int = 3) -> None:
        super().__init__(game)
        self.shape = Box(game.screen.width * .95,
                         game.screen.height * .85, 7)
        self.pos = Vector((game.screen.width - self.shape.width)/2,
                          game.screen.height * .05)
        self.enemies: list[list[Enemy]] = []
        self.enemy_direction = -1
        self.enemy_ai = True
        self.game.add_obj(self, True, True, Game.TICKED)
        self.add_enemies(enemy_cols, enemy_rows)
        self.tick_task(self.toggle_hive_ai)
        self.tick_task(self.move_enemies)
        self.tick_task(self.remove_killed_enemies)

    def remove_killed_enemies(self):
        for enemy_col in self.enemies:
            for enemy in enemy_col:
                if enemy not in self.game.ticked_objs:
                    enemy_col.remove(enemy)

    def add_enemies(self, cols, rows):
        row_padding = get_spread_spacing(Enemy.width, cols,
                                         self.shape.width * .9)
        col_padding = get_spread_spacing(Enemy.height,
                                         rows, self.shape.height * .33)
        pos = Vector(self.pos.x, self.pos.y + 2)
        for col in range(cols):
            enemy_col = []
            for row in range(rows):
                enemy_col.append(Enemy(self.game, pos))
                pos = Vector(pos.x, pos.y + Enemy.height + col_padding)
            self.enemies.append(enemy_col)
            pos = Vector(pos.x + Enemy.width + row_padding,
                         self.pos.y + 2)

    def toggle_hive_ai(self):
        if px.btnp(px.KEY_F10):
            self.enemy_ai = not self.enemy_ai

    def move_enemies(self):
        if not self.enemy_ai:
            for col in self.enemies:
                if len(col) != 0:
                    col[-1].can_attack = False
            return
        direction_change = False
        for enemy_col in self.enemies:  # check if we need to change direction
            for enemy in enemy_col:
                if not self.shape.is_inside(enemy.shape):
                    self.enemy_direction *= -1
                    direction_change = True
                    break
                if enemy.pos.y >= self.shape.scaled_pos(0, .95).y:
                    self.game.game_over()

        for enemy_col in self.enemies:  # apply motion and update attack status
            if len(enemy_col) != 0:
                enemy_col[-1].can_attack = True
            for enemy in enemy_col:
                if direction_change:
                    enemy.pos.y += enemy.speed * self.game.delta_time
                    enemy.speed += 1
                enemy.pos.x += enemy.speed * self.enemy_direction * self.game.delta_time
