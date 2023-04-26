from .shape import Shape
from .vector import Vector

import pyxel as px


class Box(Shape):
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

    def __repr__(self) -> str:
        return f"Box: {self.corners}"

    @property
    def pos(self) -> Vector:
        return self._pos

    @pos.setter
    def pos(self, value):
        if isinstance(value, Vector):
            self._pos = value
        else:
            raise TypeError(value)

    @property
    def corners(self):
        return [self.pos,
                Vector(self.pos.x, self.pos.y + self.height),
                Vector(self.pos.x + self.width, self.pos.y),
                Vector(self.pos.x + self.width, self.pos.y + self.height)]

    def is_touching(self, other_shape: Shape, not_inside: bool = True):
        if isinstance(other_shape, Box):
            for corner in other_shape.corners:
                is_x = corner.x >= self.corners[0].x
                is_x = is_x and corner.x <= self.corners[3].x
                is_y = corner.y >= self.corners[0].y
                is_y = is_y and corner.y <= self.corners[3].y
                if is_x and is_y:
                    return True
            return False

    def scaled_pos(self, width: float, height: float):
        return Vector(self.pos.x + (self.width * width),
                      self.pos.y + (self.height * height))

    # TODO: fix is_inside, its context is inverted
    def is_inside(self, other_shape: Shape):
        if isinstance(other_shape, Box):
            for corner in other_shape.corners:
                is_x = corner.x >= self.corners[0].x
                is_x = is_x and corner.x <= self.corners[3].x
                is_y = corner.y >= self.corners[0].y
                is_y = is_y and corner.y <= self.corners[3].y
                if not is_x or not is_y:
                    return False
            return True
        else:
            raise TypeError(other_shape)

    def draw(self, color: int):
        px.rect(self.pos.x, self.pos.y,
                self.width, self.height, color)
