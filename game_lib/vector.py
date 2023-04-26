from __future__ import annotations
import math

__all__ = ["Vector"]


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def clamp_x(self, mn: float, mx: float) -> Vector:
        x = min(max(self.x, mn), mx)
        return Vector(x, self.y)

    def clamp_y(self, mn: float, mx: float) -> Vector:
        y = min(max(self.y, mn), mx)
        return Vector(self.x, y)

    def clamp(self, mn: float, mx: float) -> Vector:
        return self.clamp_x(mn, mx).clamp_y(mn, mx)

    def normalize(self) -> Vector:
        x = self.x
        y = self.y
        if self.x != 0 or self.y != 0:
            x /= self.magnitude
            y /= self.magnitude
        return Vector(x, y)

    def __add__(self, o: Vector) -> Vector:
        return Vector(self.x + o.x, self.y + o.y)

    def __sub__(self, o: Vector) -> Vector:
        return Vector(self.x - o.x, self.y - o.y)

    def __mul__(self, o: float | Vector) -> Vector:
        if isinstance(o, Vector):
            # this is a scalar value of how similar the two vectors are.
            # 1 is the exact same, -1 is exact opposite.
            return self.x * o.x + self.y * o.y
        else:
            return Vector(self.x * o, self.y * o)

    def __div__(self, o: float) -> Vector:
        return Vector(self.x / o, self.y / o)

    def __repr__(self) -> str:
        return f"Vector(x={round(self.x, 1)},y={round(self.y, 1)})"

    def __str__(self) -> str:
        return f"x={round(self.x, 1)},y={round(self.y, 1)}"
