import pyxel as px
from . import GameObject, Game, Box, Vector

CENTERED = 0
RIGHT = 1
LEFT = -1
TOP = -1
BOTTOM = 1

__all__ = [CENTERED, RIGHT, LEFT, TOP, BOTTOM, "TextBox"]


class TextBox(GameObject):
    def __init__(self, game: Game, text: str, color: int) -> None:
        super().__init__(game)
        self.text = text
        self.color = color
        size = self.calculate_size()
        self.shape = Box(size[0], size[1])

    def place(self, horizontal_pos: int, vertical_pos: int):
        if horizontal_pos == -1:
            horizontal_pos = 2
        elif horizontal_pos == 0:
            horizontal_pos = (self.game.screen.width - self.shape.width)/2
        elif horizontal_pos == 1:
            horizontal_pos = self.game.screen.width - self.shape.width

        if vertical_pos == -1:
            vertical_pos = 2
        elif vertical_pos == 0:
            vertical_pos = (self.game.screen.height - self.shape.height)/2
        elif vertical_pos == 1:
            vertical_pos = self.game.screen.height - self.shape.height
        self.pos = Vector(horizontal_pos, vertical_pos)

    def calculate_size(self):
        length = 0
        width = 0
        rows = self.text.split()
        for row in rows:
            width += 5
            for char in row:
                length += 4
        return length, width

    def draw(self):
        px.text(self.pos.x, self.pos.y, self.text, self.color)
