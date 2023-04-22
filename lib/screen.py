from . import Vector, Box
import pyxel as px


class Screen(Box):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
        self.pos = Vector(0, 0)
        self.aspect_ratio = width / height

    def scaled_pos(self, x: float, y: float) -> Vector:
        return Vector(self.width * x, self.height * y)

    def draw_debug(self, game_obj: object,
                   color: int = 11, obj_color: int = 10,
                   background_color: int = 1):
        text_padding = 2

        # height of the text block in pixels
        debug_height = (len(game_obj.__dict__.keys()) + 1) * 7

        # pos to start the debug text block in
        debug_pos = Vector(1, self.height - debug_height)

        px.rect(0, debug_pos.y - text_padding, self.width,
                debug_height + text_padding, background_color)
        px.text(debug_pos.x, debug_pos.y, game_obj.__repr__(), obj_color)
        debug_pos += Vector(7, 7)
        for key in game_obj.__dict__.keys():
            value = game_obj.__dict__[key]
            if isinstance(value, float):
                value = round(value, 2)
            px.text(debug_pos.x, debug_pos.y, f"{key}={value}", color)
            debug_pos += Vector(0, 7)
