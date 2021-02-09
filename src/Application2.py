from src.GymEnvironment import GymEnvironment
from src.exception.InvalidActionError import InvalidActionError
from src.ui.Button import Button
from src.ui.Checkbox import Checkbox
from src.ui.Drawable import Drawable
from src.ui.DropdownButton import DropdownButton
from src.ui.MenuButton import MenuButton
from src.ui.Window import Window
import numpy as np
from numpy import ndarray
import cv2

from src.util.MatrixUtils import MatrixUtils


class Application2(GymEnvironment):

    def __init__(self):
        self.__all_buttons = []
        main_window = self.__init_components()
        self.__windows = [main_window]
        self.__frame_buffer = main_window.current_matrix.copy()
        self.__width = main_window.width
        self.__height = main_window.height
        self.__should_re_stack = False
        self.__done = False
        self.__windows_to_be_removed = []

    def __init_components(self) -> Window:
        # Load images
        # --------------------------------------------------------------------------------------------------
        main_window_array = MatrixUtils.get_numpy_array_of_image('resources/drawables/main_window.png')

        close_button_large_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/close_window_button_large_unclicked.png')

        uber_window_array = MatrixUtils.get_numpy_array_of_image('resources/drawables/window_über.png')

        close_uber_window_button_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/close_über_window_button.png')
        close_button_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/close_window_button_unclicked.png')

        preferences_window_array = MatrixUtils.get_numpy_array_of_image('resources/drawables/window_preferences.png')
        preferences_window_abbrechen_button_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/button_abbrechen_unclicked.png')

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

        menu_button_other_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_button_1.png')
        menu_button_other_clicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_button_1_clicked.png')

        menu_button_preferences_unclicked_array = MatrixUtils.get_numpy_array_of_image(
            'resources/drawables/menu_button_preferences_unclicked.png')

        # --------------------------------------------------------------------------------------------------

        # Define click listeners
        # --------------------------------------------------------------------------------------------------
        def open_uber(btn: Button):
            # Close dropdown menu first
            self.remove_window()
            self.add_window(uber_window)

        def open_preferences(btn: Button):
            # Close dropdown menu first
            self.remove_window()
            self.add_window(preferences_window)

        """
        def hide_button(btn: Button):
            self.change_visibility(btn, not btn.visible)
        """

        def close_window(btn: Button):
            self.remove_window()

        def close_application(btn: Button):
            self.__done = True

        # --------------------------------------------------------------------------------------------------

        # Initialize components
        # --------------------------------------------------------------------------------------------------
        next_pos = 0
        main_window_children = []

        app_close_button = Button(close_button_large_array, np.array([380, 0]), reward=2,
                                  on_click_listener=close_application)
        self.__all_buttons.append(app_close_button)
        main_window_children.append(app_close_button)

        dropdown_button_datei_children = []
        for i in range(0, 10):
            button = MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array, reward=2)
            dropdown_button_datei_children.append(button)
            self.__all_buttons.append(button)

        preferences_button = MenuButton(menu_button_preferences_unclicked_array,
                                        reward=2,
                                        on_click_listener=open_preferences)
        dropdown_button_datei_children.append(preferences_button)
        self.__all_buttons.append(preferences_button)

        dropdown_button_datei = DropdownButton(dropdown_datei_unclicked_array, np.array([next_pos, 12]),
                                               dropdown_button_datei_children, self,
                                               dropdown_datei_clicked_array, reward=2)
        self.__all_buttons.append(dropdown_button_datei)

        next_pos += dropdown_button_datei.width
        main_window_children.append(dropdown_button_datei)

        dropdown_button_anzeigen_children = []
        for i in range(0, 3):
            button = MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array, reward=2)
            dropdown_button_anzeigen_children.append(button)
            self.__all_buttons.append(button)

        dropdown_button_anzeigen = DropdownButton(dropdown_anzeigen_unclicked_array,
                                                  np.array([next_pos, 12]),
                                                  dropdown_button_anzeigen_children, self,
                                                  dropdown_anzeigen_clicked_array, reward=2)
        self.__all_buttons.append(dropdown_button_anzeigen)

        next_pos += dropdown_button_anzeigen.width
        main_window_children.append(dropdown_button_anzeigen)

        dropdown_button_navigation_children = []
        for i in range(0, 4):
            button = MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array, reward=2)
            dropdown_button_navigation_children.append(button)
            self.__all_buttons.append(button)

        dropdown_button_navigation = DropdownButton(dropdown_navigation_unclicked_array,
                                                    np.array([next_pos, 12]),
                                                    dropdown_button_navigation_children, self,
                                                    dropdown_navigation_clicked_array, reward=2)
        self.__all_buttons.append(dropdown_button_navigation)

        next_pos += dropdown_button_navigation.width
        main_window_children.append(dropdown_button_navigation)

        dropdown_button_tools_children = []
        for i in range(0, 2):
            button = MenuButton(menu_button_other_unclicked_array, menu_button_other_clicked_array, reward=2)
            dropdown_button_tools_children.append(button)
            self.__all_buttons.append(button)

        dropdown_button_tools = DropdownButton(dropdown_tools_unclicked_array,
                                               np.array([next_pos, 12]),
                                               dropdown_button_tools_children, self,
                                               dropdown_tools_clicked_array, reward=2)
        self.__all_buttons.append(dropdown_button_tools)

        next_pos += dropdown_button_tools.width
        main_window_children.append(dropdown_button_tools)

        menu_button_uber = MenuButton(menu_button_uber_unclicked_array, reward=2,
                                      on_click_listener=open_uber)
        self.__all_buttons.append(menu_button_uber)

        dropdown_button_hilfe = DropdownButton(dropdown_hilfe_unclicked_array,
                                               np.array([next_pos, 12]),
                                               [menu_button_uber], self,
                                               dropdown_hilfe_clicked_array, reward=2)
        self.__all_buttons.append(dropdown_button_hilfe)

        main_window_children.append(dropdown_button_hilfe)

        preferences_window_children = []
        preferences_window_checkbox_coords = [[136, 25], [169, 102], [169, 113], [169, 125], [155, 145], [148, 206],
                                              [148, 218], [148, 230], [312, 64], [312, 82], [312, 100], [312, 118],
                                              [312, 136], [312, 154], [312, 172], [312, 190], [312, 208], [312, 226]]

        for coord in preferences_window_checkbox_coords:
            preferences_window_checkbox = Checkbox(np.array(coord), reward=2)
            preferences_window_children.append(preferences_window_checkbox)
            self.__all_buttons.append(preferences_window_checkbox)

        preferences_window_abbrechen_button = Button(preferences_window_abbrechen_button_array, np.array([315, 248]),
                                                     reward=2,
                                                     on_click_listener=close_window)
        self.__all_buttons.append(preferences_window_abbrechen_button)
        preferences_window_children.append(preferences_window_abbrechen_button)
        preferences_window = Window(preferences_window_array, preferences_window_children, np.array([2, 2]))

        close_button = Button(close_button_array, np.array([80, 1]), reward=2, on_click_listener=close_window)
        self.__all_buttons.append(close_button)
        close_uber_button = Button(close_uber_window_button_array, np.array([1, 86]), reward=2,
                                   on_click_listener=close_window)
        self.__all_buttons.append(close_uber_button)
        uber_window = Window(uber_window_array, [close_uber_button, close_button], np.array([273, 123]))

        # --------------------------------------------------------------------------------------------------
        # Return main window
        return Window(main_window_array, main_window_children, np.array([0, 0]))

    @property
    def frame_buffer(self):
        return self.__frame_buffer

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def step(self, action: ndarray) -> (ndarray, int, bool):
        if type(action) is not np.ndarray:
            raise InvalidActionError('Invalid Action')

        reward = 0
        number_of_windows_to_be_removed = 0

        # Click on windows starting with the topmost window down to the window at the bottom
        for i in range(-1, -len(self.__windows) - 1, -1):
            index = i + number_of_windows_to_be_removed
            reward, window_includes_point, clicked_child_component_matrix, clicked_child_component_coords = self.__windows[index].click(action)
            if window_includes_point:
                if clicked_child_component_matrix is not None:
                    # Blit the changed component directly on the frame buffer, only if the clicked component is
                    # in the topmost window
                    if not self.__should_re_stack:
                        MatrixUtils.blit_image_inplace(self.__frame_buffer, clicked_child_component_matrix,
                                                       clicked_child_component_coords)
                break
            else:
                if self.__windows[index].modal:
                    break
                elif self.__windows[index].auto_close:
                    # Save the removed window for future reference
                    removed_window = self.remove_window()
                    self.__windows_to_be_removed.append(removed_window)
                    number_of_windows_to_be_removed += 1

        if self.__should_re_stack:
            self.__frame_buffer = self.__stack_windows()

        # Reset internal state
        self.__should_re_stack = False
        self.__windows_to_be_removed.clear()
        return self.__frame_buffer, reward, self.__done

    def add_window(self, window: Window):
        self.__windows.append(window)
        MatrixUtils.blit_image_inplace(self.__frame_buffer, window.current_matrix, window.relative_coordinates)

    def remove_window(self) -> Window:
        removed = self.__windows.pop()
        removed.reset()
        self.__windows[-1].reset()
        self.__should_re_stack = True
        return removed

    def change_visibility(self, drawable: Drawable, value: bool):
        drawable.visible = value
        self.__windows[-1].draw_self()
        self.__should_re_stack = True

    def reset(self) -> ndarray:
        self.__all_buttons = []
        main_window = self.__init_components()
        self.__windows = [main_window]
        self.__frame_buffer = main_window.current_matrix.copy()
        self.__should_re_stack = False
        self.__done = False
        return self.__frame_buffer

    def close(self):
        pass

    def render(self):
        cv2.imshow('App', np.transpose(self.__frame_buffer, (1, 0, 2)))
        cv2.waitKey(0)

    def get_progress(self) -> ndarray:
        progress_vector = []
        for button in self.__all_buttons:
            if button.reward_given:
                progress_vector.append(1)
            else:
                progress_vector.append(0)
        return np.array(progress_vector)

    def is_window_going_to_be_removed(self, window: Window) -> bool:
        for win in self.__windows_to_be_removed:
            if win == window:
                return True
        return False

    def __stack_windows(self) -> ndarray:
        final = self.__windows[0].current_matrix.copy()
        for k in range(1, len(self.__windows)):
            MatrixUtils.blit_image_inplace(final, self.__windows[k].current_matrix,
                                           self.__windows[k].relative_coordinates)
        return final
