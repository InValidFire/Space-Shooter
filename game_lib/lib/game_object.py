from __future__ import annotations
from itertools import product
from typing import Type

from . import Vector
from . import Shape
from . import Game

IS_TOUCHED = 0
IS_CONTAINED = 1

__all__ = ["IS_TOUCHED", "IS_CONTAINED", "GameObject"]


class GameObject:
    def __init__(self, game: Game) -> None:
        self.game = game

        # known objects of given type it can collide with
        self._collision_objs = []

        # list containing a list of [Class, Int]
        # matching IS_TOUCHED or IS_CONTAINED
        self._collision_types: list[Type, int] = []
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

    def set_collision_types(self, collision_list: list[GameObject, int]):
        self._collision_types = collision_list

    def add_collision_check(self, obj_type: Type, contained_or_touched: int):
        self._collision_types.append([obj_type, contained_or_touched])

    def check_collisions(self):
        self._collision_objs = []
        for obj, col_type in product(self.game.ticked_objs,
                                     self._collision_types):
            if isinstance(obj, col_type[0]) and obj is not self:
                self._collision_objs.append([obj, col_type[1]])
        self.collisions = []
        for obj in self._collision_objs:
            if obj[1] == 1:
                if obj[0].shape.is_inside(self.shape):
                    self.collisions.append(obj[0])
            elif obj[1] == 0:
                if self.shape.is_touching(obj[0].shape):
                    self.collisions.append(obj[0])
        return self.collisions

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
