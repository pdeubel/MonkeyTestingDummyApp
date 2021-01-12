from typing import Callable

from numpy import ndarray

from src.ui.Button import Button
from src.util.MatrixUtils import MatrixUtils

array_clicked = MatrixUtils.get_numpy_array_of_image('resources/drawables/chk_clicked.png')
array_unclicked = MatrixUtils.get_numpy_array_of_image('resources/drawables/chk_unclicked.png')
array_clicked_dis = MatrixUtils.get_numpy_array_of_image('resources/drawables/chk_clicked_dis.png')
array_unclicked_dis = MatrixUtils.get_numpy_array_of_image('resources/drawables/chk_unclicked_dis.png')


class Checkbox(Button):

    def __init__(self,
                 relative_coordinates: ndarray,
                 reward: int,
                 on_click_listener: Callable[[Button], None] = lambda b: None):
        super().__init__(array_unclicked,
                         relative_coordinates,
                         array_clicked,
                         array_clicked_dis,
                         reward,
                         on_click_listener,
                         False)
