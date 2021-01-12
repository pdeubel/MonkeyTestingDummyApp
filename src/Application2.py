from src.GymEnvironment import GymEnvironment
from src.exception.InvalidActionError import InvalidActionError
from src.ui.Button import Button
from src.ui.Drawable import Drawable
from src.ui.DropdownButton import DropdownButton
from src.ui.MenuButton import MenuButton
from src.ui.Window import Window
import numpy as np

from src.util.MatrixUtils import MatrixUtils


class Application2(GymEnvironment):

    def __init__(self):
        window = self.__init_components()
        self.__windows = [window]
        self.__current_matrix = window.current_matrix
        self.__width = window.width
        self.__height = window.height
        self.__re_stack = False
        self.__active_index = -1

    def __init_components(self) -> Window:
        # Load images
        # --------------------------------------------------------------------------------------------------
        main_window_array = MatrixUtils.get_numpy_array_of_image('resources/drawables/main_window.png')

        uber_window_array = MatrixUtils.get_numpy_array_of_image('resources/drawables/window_über.png')
        close_uber_window_button_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/close_über_window_button.png')
        close_button_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/close_window_button_unclicked.png')

        dropdown_datei_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_datei_unclicked.png')
        dropdown_datei_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_datei_clicked.png')
        dropdown_anzeigen_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_anzeigen_unclicked.png')
        dropdown_anzeigen_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_anzeigen.png')
        dropdown_hilfe_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_hilfe_unclicked.png')
        dropdown_hilfe_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_hilfe_clicked.png')
        dropdown_navigation_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_navigation_unclicked.png')
        dropdown_navigation_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_navigation_clicked.png')
        dropdown_tools_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_tools_unclicked.png')
        dropdown_tools_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/drpdwn_tools_clicked.png')

        menu_button_uber_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_über_unclicked.png')
        menu_button_uber_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_über_clicked.png')

        menu_button_other_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_button_1.png')
        menu_button_other_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_button_1_clicked.png')

        # --------------------------------------------------------------------------------------------------

        # Define click listeners
        # --------------------------------------------------------------------------------------------------
        def open_uber(btn: Button):
            self.add_window(uber_window)

        def hide_button(btn: Button):
            pass
            # self.change_visibility(button2, not button2.visible)

        def close_window(btn: Button):
            self.remove_window()

        # --------------------------------------------------------------------------------------------------

        # Initialize components
        # --------------------------------------------------------------------------------------------------
        close_button = Button(close_button_array, np.array([242, 1]), reward=2, on_click_listener=close_window)
        close_uber_button = Button(close_uber_window_button_array, np.array([2, 259]), reward=2, on_click_listener=close_window)
        uber_window = Window(uber_window_array, [close_uber_button, close_button], np.array([818, 369]))

        next_pos = 0
        main_window_children = []

        dropdown_button_datei_children = []
        for i in range(0, 10):
            dropdown_button_datei_children.append(
                MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array,
                           reward=2))

        dropdown_button_datei = DropdownButton(dropdown_datei_unclicked_array, np.array([next_pos, 37]),
                                               dropdown_button_datei_children, self,
                                               dropdown_datei_clicked_array, reward=2)

        next_pos += dropdown_button_datei.width
        main_window_children.append(dropdown_button_datei)

        dropdown_button_anzeigen_children = []
        for i in range(0, 3):
            dropdown_button_anzeigen_children.append(
                MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array,
                           reward=2))

        dropdown_button_anzeigen = DropdownButton(dropdown_anzeigen_unclicked_array,
                                                  np.array([next_pos, 37]),
                                                  dropdown_button_anzeigen_children, self,
                                                  dropdown_anzeigen_clicked_array, reward=2)

        next_pos += dropdown_button_anzeigen.width
        main_window_children.append(dropdown_button_anzeigen)

        dropdown_button_navigation_children = []
        for i in range(0, 4):
            dropdown_button_navigation_children.append(
                MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array,
                           reward=2))

        dropdown_button_navigation = DropdownButton(dropdown_navigation_unclicked_array,
                                                    np.array([next_pos, 37]),
                                                    dropdown_button_navigation_children, self,
                                                    dropdown_navigation_clicked_array, reward=2)

        next_pos += dropdown_button_navigation.width
        main_window_children.append(dropdown_button_navigation)

        dropdown_button_tools_children = []
        for i in range(0, 2):
            dropdown_button_tools_children.append(
                MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array,
                           reward=2))

        dropdown_button_tools = DropdownButton(dropdown_tools_unclicked_array,
                                               np.array([next_pos, 37]),
                                               dropdown_button_tools_children, self,
                                               dropdown_tools_clicked_array, reward=2)

        next_pos += dropdown_button_tools.width
        main_window_children.append(dropdown_button_tools)

        menu_button_uber = MenuButton(menu_button_uber_unclicked_array, menu_button_uber_clicked_array, reward=2,
                                      on_click_listener=open_uber)

        dropdown_button_hilfe = DropdownButton(dropdown_hilfe_unclicked_array,
                                               np.array([next_pos, 37]),
                                               [menu_button_uber], self,
                                               dropdown_hilfe_clicked_array, reward=2)

        main_window_children.append(dropdown_button_hilfe)

        # --------------------------------------------------------------------------------------------------
        # Return main window
        return Window(main_window_array, main_window_children, np.array([0, 0]))

    @property
    def current_matrix(self):
        return self.__current_matrix

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def step(self, action):
        if type(action) is not np.ndarray:
            raise InvalidActionError('Invalid Action')

        reward = 0
        number_of_del_windows = 0
        # Click on windows starting with the topmost window down to the window at the bottom
        for i in range(-1, -len(self.__windows) - 1, -1):
            index = i + number_of_del_windows
            reward, includes_point, mat, coord = self.__windows[index].click(action, np.array([0, 0]))
            if includes_point:
                self.__current_matrix = MatrixUtils.blit_image(self.__current_matrix, mat, coord)
                break
            else:
                if self.__windows[index].modal:
                    break
                else:
                    # Check if the click landed on somewhere in the window. If yes, don't close the non modal window
                    # If no AND if auto_close is true -> change the active index to the index of the window below and
                    # continue with the loop
                    if not MatrixUtils.includes_point(action, self.__windows[index].relative_coordinates,
                                                      self.__windows[index].width, self.__windows[index].height):
                        if self.__windows[index].auto_close:
                            removed = self.__windows.pop()
                            removed.reset()
                            self.__windows[-1].reset()
                            self.__re_stack = True
                            number_of_del_windows += 1
                    else:
                        break

        if self.__re_stack:
            self.__current_matrix = self.__stack_windows()

        # Reset internal state
        self.__re_stack = False
        self.__active_index = -1
        return self.__current_matrix, reward

    def add_window(self, window: Window):
        """
        if self.__active_index == -1:
            temp_i = len(self.__windows)
        else:
            temp_i = self.__active_index + 1
        """
        self.__windows.append(window)
        self.__re_stack = True

    def remove_window(self):
        removed = self.__windows.pop()
        removed.reset()
        self.__windows[-1].reset()
        # self.__windows[self.__active_index].reset()
        # del self.__windows[self.__active_index]
        # self.__windows[self.__active_index].reset()
        self.__re_stack = True

    def change_visibility(self, drawable: Drawable, value: bool):
        drawable.visible = value
        self.__windows[-1].update_matrix()
        self.__re_stack = True

    def reset(self):
        pass

    def close(self):
        pass

    def __remove_non_modals(self):
        """
        Remove all windows starting from the top and stopping at the active index
        """
        for i in range(-1, self.__active_index, -1):
            removed = self.__windows.pop()
            removed.reset()
        self.__windows[-1].reset()

    def __stack_windows(self) -> np.ndarray:
        # if len(self.__windows) == 1:
            # self.__windows[0].reset()
        final = self.__windows[0].current_matrix
        for k in range(1, len(self.__windows)):
            # if k == len(self.__windows) - 1:
                # self.__windows[k].reset()
            final = MatrixUtils.blit_image(final,
                                           self.__windows[k].current_matrix,
                                           self.__windows[k].relative_coordinates)
        return final
