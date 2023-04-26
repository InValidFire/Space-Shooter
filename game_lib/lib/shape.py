from __future__ import annotations

from abc import ABC, abstractmethod
from .vector import Vector

__all__ = ["Shape"]


class Shape(ABC):
    @property
    def color(self) -> bool:
        if "_color" not in self.__dict__:
            self._color = 1
        return self._color

    @color.setter
    def color(self, value: int):
        if not isinstance(value, int):
            raise TypeError(value)
        if value > 16:
            raise ValueError(value)
        self._color = value

    @property
    def visible(self) -> bool:
        if "_visible" not in self.__dict__:
            self._visible = False
        return self._visible

    @visible.setter
    def visible(self, value: bool):
        if isinstance(value, bool):
            self._visible = value
        else:
            raise TypeError(value)

    @property
    @abstractmethod
    def pos(self) -> Vector:
        pass

    @pos.setter
    @abstractmethod
    def pos(self, value):
        pass

    @abstractmethod
    def is_touching(self, other_shape: Shape):
        pass

    @abstractmethod
    def draw(self, color: int):
        pass
