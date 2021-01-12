from numpy import ndarray
import numpy as np
from typing import List

from src.ui.CompositeDrawable import CompositeDrawable
from src.ui.Drawable import Drawable
from src.util.MatrixUtils import MatrixUtils


class Window(CompositeDrawable):
    """
    A Window is a :class:`CompositeDrawable` which can only be at the top of the component hierarchy
    """

    def __init__(self, matrix_self: ndarray, children: List[Drawable], relative_coordinates: ndarray,
                 modal: bool = True, auto_close: bool = False):
        super().__init__(matrix_self, children, relative_coordinates, matrix_self.shape[0], matrix_self.shape[1])
        self.__current_matrix = self.draw_self()
        self.__modal = modal
        self.__auto_close = auto_close

    @property
    def current_matrix(self):
        return self.__current_matrix

    @property
    def modal(self):
        return self.__modal

    @property
    def auto_close(self):
        return self.__auto_close

    def update_matrix(self):
        self.__current_matrix = self.draw_self()

    def click(self, click_coordinates: ndarray, parent_coordinates: ndarray) -> (int, bool, ndarray, ndarray):
        if self.visible:
            if MatrixUtils.includes_point(click_coordinates, self.relative_coordinates, self.width,
                                          self.height):
                for child in self.children:
                    reward, includes_point, mat, coord = child.click(click_coordinates, self.relative_coordinates)
                    if includes_point:
                        self.__blit_single_drawable(mat, coord)
                        return reward, includes_point, mat, coord

        return 0, False, None, None

    def draw_self(self, parent_coordinates: ndarray = np.array([0, 0]), parent_matrix: ndarray = None) -> ndarray:
        coords = parent_coordinates + self.relative_coordinates
        if parent_matrix is None:
            parent_matrix = self.matrix_self.copy()
            coords = parent_coordinates

        if not self.visible:
            return parent_matrix

        temp = MatrixUtils.blit_image(parent_matrix, self.matrix_self,
                                      coords)
        for child in self.children:
            temp = child.draw_self(coords, temp)

        return temp

    def reset(self) -> bool:
        comp_changed = super().reset()
        if comp_changed:
            self.__current_matrix = self.draw_self()
        return comp_changed

    def __blit_single_drawable(self, component_matrix: ndarray, abs_coords: ndarray):
        self.__current_matrix = MatrixUtils.blit_image(
            self.__current_matrix,
            component_matrix,
            abs_coords - self.relative_coordinates)
