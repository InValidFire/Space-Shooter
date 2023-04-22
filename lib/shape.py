from __future__ import annotations

from abc import ABC, abstractmethod
from .vector import Vector


class Shape(ABC):
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
    def draw(self):
        pass
