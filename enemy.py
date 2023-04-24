from lib import Vector, GameObject, Box
import pyxel as px


def get_spread_spacing(width_of_n, n, length):
    return (length - width_of_n)/(n-1) - width_of_n


class Enemy(GameObject):
    direction = 1
    direction_lock = False

    def __init__(self, game, pos: Vector, size: int, enemy_area: Box):
        super().__init__(game)
        self.shape = Box(size, size)
        self.speed = 60  # pixels/sec
        self.pos = pos
        self.enemy_area = enemy_area
        self.game.add_obj(self, True)
        self.ai_enabled = False
        self.tick_task(self.move)
        self.tick_task(self.toggle_ai)

    def draw(self):
        self.shape.draw(10)

    def move(self):
        if not self.ai_enabled:
            return
        Enemy.direction_lock = False
        if not self.enemy_area.is_touching(self.shape):
            Enemy.direction_lock = False
        if self.enemy_area.is_touching(self.shape) and not Enemy.direction_lock:
            Enemy.direction *= -1
            Enemy.direction_lock = True
        self.pos.x += (self.speed * self.direction) * self.game.delta_time

    def toggle_ai(self):
        if px.btnp(px.KEY_F10) and self.game.is_debug:
            self.ai_enabled = not self.ai_enabled

    @staticmethod
    def setup(game, size: int = 16, rows: int = 12, cols: int = 3):
        screen = game.screen
        enemy_area = Box(screen.width - (size * 2), screen.height * .33)
        enemy_area.pos = Vector((screen.width - enemy_area.width)/2, (screen.height - enemy_area.height)/2)
        row_padding = get_spread_spacing(size, rows, enemy_area.width - enemy_area.width/2)
        col_padding = get_spread_spacing(size, cols, enemy_area.height - 4)
        starting_pos = Vector(enemy_area.pos.x, enemy_area.pos.y + 2)
        for row in range(rows):
            starting_pos = Vector(starting_pos.x + size + row_padding, enemy_area.pos.y + 2)
            for col in range(cols):
                Enemy(game, starting_pos, size, enemy_area)
                starting_pos = Vector(starting_pos.x, starting_pos.y + size + col_padding)
