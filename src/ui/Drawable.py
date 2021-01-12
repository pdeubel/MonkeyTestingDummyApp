from abc import ABC, abstractmethod

from numpy import ndarray


class Drawable(ABC):
    """

    """
    @abstractmethod
    def __init__(self, relative_coordinates: ndarray, width: int, height: int):
        self.__relative_coordinates = relative_coordinates
        self.__width = width
        self.__height = height
        self.__visible = True

    @property
    def relative_coordinates(self):
        return self.__relative_coordinates

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, value):
        self.__visible = value

    @abstractmethod
    def click(self, click_coordinates: ndarray, parent_coordinates: ndarray) -> (int, bool, ndarray, ndarray):
        pass

    @abstractmethod
    def draw_self(self, parent_coordinates: ndarray, parent_matrix: ndarray) -> ndarray:
        pass

    @abstractmethod
    def reset(self) -> bool:
        pass
