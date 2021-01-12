from numpy import ndarray
from typing import List

from src.ui.Drawable import Drawable
from abc import ABC, abstractmethod


class CompositeDrawable(Drawable, ABC):
    """
    A CompositeDrawable is a :class:`Drawable` which can contain other :class:`Drawable`'s as its children
    """

    @abstractmethod
    def __init__(self, matrix_self: ndarray, children: List[Drawable], relative_coordinates: ndarray, width: int,
                 height: int):
        super().__init__(relative_coordinates, width, height)
        self.__matrix_self = matrix_self
        self.__children = children

    @property
    def children(self):
        return self.__children

    @property
    def matrix_self(self):
        return self.__matrix_self

    def reset(self) -> bool:
        comp_changed = False
        for child in self.__children:
            res = child.reset()
            comp_changed = comp_changed or res
        return comp_changed
