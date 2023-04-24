from __future__ import annotations

from . import Vector
from . import Shape

IS_TOUCHED = 0
IS_CONTAINED = 1


class GameObject:
    def __init__(self, game) -> None:
        self.game = game
        self._collision_objs = []
        self.collisions = []
        self._tasks = []

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        if isinstance(value, Shape):
            self._shape = value
        else:
            raise TypeError(value)

    @property
    def pos(self):
        return self._pos

    def set_collisions(self, collision_list: list[GameObject, int]):
        self._collision_objs = collision_list

    def add_collision_check(self, obj: GameObject, collision_type: int):
        self._collision_objs.append([obj, collision_type])

    def check_collisions(self):
        collisions = []
        for obj in self._collision_objs:
            if obj[1] == 1:
                if obj[0].shape.is_inside(self.shape):
                    collisions.append(obj[0])
            elif obj[1] == 0:
                if obj[0].shape.is_touching(self.shape):
                    collisions.append(obj[0])
        return collisions

    def tick_task(self, f):
        self._tasks.append(f)

    def untick_task(self, f):
        self._tasks.remove(f)

    def update(self):
        for task in self._tasks:
            task()

    @pos.setter
    def pos(self, value: Vector):
        if not isinstance(value, Vector):
            raise TypeError(value)
        else:
            self._pos = value
            self.shape.pos = self._pos
        # if isinstance(value, Vector):
        #     screen_width = self.app.screen.width
        #     screen_height = self.app.screen.height
        #     value = value.clamp_x(0, screen_width - self.shape.width)
        #     self._pos = value.clamp_y(0, screen_height - self.shape.height)
        #     self.shape.pos = self._pos

    def is_touching(self, gobj: GameObject):
        return self.shape.is_touching(gobj.shape)
