from numpy import ndarray
import numpy as np
from typing import List

from src import Application2
from src.ui.Button import Button
from src.ui.MenuButton import MenuButton
from src.ui.Window import Window
from src.util.MatrixUtils import MatrixUtils


class DropdownButton(Button):

    def __init__(self,
                 matrix_unclicked: ndarray,
                 relative_coordinates: ndarray,
                 menu_buttons: List[MenuButton],
                 app: Application2,
                 matrix_clicked: ndarray = None,
                 matrix_disabled: ndarray = None,
                 reward: int = 0):
        """
        A :class:`Button` which opens a dropdown menu when clicked. The dropdown menu consists of :class:`MenuButton`'s

        :param matrix_unclicked: Image matrix of the button in unclicked state
        :param relative_coordinates: Coordinates of the button relative to its parent Drawable
        :param menu_buttons: A List of MenuButton's to be shown on the dropdown menu
        :param app: The main application object
        :param matrix_clicked: Image matrix of the button in clicked state
        :param matrix_disabled: Image matrix of the button in disabled state
        :param reward: The amount of reward this button generates when clicked for the first time
        """

        self.__parent_coords = None
        self.__menu = None
        dropdown_menu_width, dropdown_menu_height = self.__calculate_menu_dimensions(menu_buttons)
        background_matrix = MatrixUtils.get_blank_image_as_numpy_array((160, 160, 160), dropdown_menu_width + 2, dropdown_menu_height + 2)

        # Set relative positions of menu buttons
        menu_button_pos = np.array([1, 1])
        for button in menu_buttons:
            button.relative_coordinates = menu_button_pos
            menu_button_pos = menu_button_pos + np.array([0, button.height])

        def on_click_listener(btn: Button):
            # Button is clicked while its dropdown menu was active -> Make button unclicked instead of opening the menu
            if app.is_window_going_to_be_removed(self.__menu):
                self.clicked = False
            else:
                self.__menu = Window(background_matrix, menu_buttons,
                                     self.__parent_coords + self.relative_coordinates + np.array([0, self.height]),
                                     False,
                                     True)
                app.add_window(self.__menu)

        super().__init__(matrix_unclicked, relative_coordinates, matrix_clicked, matrix_disabled, reward,
                         on_click_listener)

    def click(self, click_coordinates: ndarray, parent_coordinates: ndarray) -> (int, bool, ndarray, ndarray):
        # Capture the parent coordinates here, since the children don't know their parents
        self.__parent_coords = parent_coordinates
        return super().click(click_coordinates, parent_coordinates)

    def __calculate_menu_dimensions(self, menu_buttons: List[Button]):
        width, height = 0, 0
        for button in menu_buttons:
            height = height + button.height
            if button.width > width:
                width = button.width
        return width, height
