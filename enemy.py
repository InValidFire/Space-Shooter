from lib import Vector, GameObject, Box


class Enemy(GameObject):
    def __init__(self, game, pos: Vector, size: int):
        super().__init__(game)
        self.shape = Box(size, size)
        self.speed = 60  # pixels/sec
        self.pos = pos
        self.left_cap = self.pos.x - self.shape.width/2  # x is not centered.
        self.right_cap = self.pos.x + self.shape.width
        self.game.add_obj(self, True)
        self.direction = 1

    def draw(self):
        self.shape.draw(10)

    def update(self):
        if self.pos.x <= self.left_cap or self.pos.x >= self.right_cap:
            self.direction *= -1
        self.pos.x += (self.speed * self.direction) * self.game.delta_time

    @staticmethod
    def setup(app, size: int = 16, rows: int = 12, cols: int = 3):
        screen = app.screen
        enemy_area = int(screen.width - (size * 2))
        row_padding = (enemy_area/rows)
        col_padding = int((screen.height * .33) - (size * 2))/cols
        for row in range(rows):
            row = int(row * row_padding + row_padding/2)
            for col in range(cols):
                col = int(col * col_padding + col_padding/2)
                pos = Vector(row, col)
                Enemy(app, pos, size)
