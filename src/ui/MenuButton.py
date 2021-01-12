from collections import Callable

from numpy import ndarray
import numpy as np

from src.ui.Button import Button


class MenuButton(Button):

    def __init__(self,
                 matrix_unclicked: ndarray,
                 matrix_clicked: ndarray = None,
                 matrix_disabled: ndarray = None,
                 reward: int = 0,
                 on_click_listener: Callable[[Button], None] = lambda b: None,
                 resettable: bool = True):
        super().__init__(matrix_unclicked, np.array([0, 0]), matrix_clicked, matrix_disabled, reward, on_click_listener,
                         resettable)

    @property
    def relative_coordinates(self):
        return self.__relative_coordinates

    @relative_coordinates.setter
    def relative_coordinates(self, value):
        self.__relative_coordinates = value
