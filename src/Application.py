from src.GymEnvironment import GymEnvironment
from src.exception.InvalidActionError import InvalidActionError
from src.ui.Window import Window
import numpy as np

from src.util.MatrixUtils import MatrixUtils


class Application(GymEnvironment):

    def __init__(self, window: Window):
        self.__windows = [window]
        initial_window = window.draw_self(np.array([0, 0]), window.matrix_self)
        self.__windows_matrices = [initial_window]
        self.__current_matrix = initial_window.copy()
        self.__width = window.width
        self.__height = window.height

    @property
    def current_matrix(self):
        return self.__current_matrix

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def add_window(self, window: Window):
        self.__windows.append(window)
        self.__windows_matrices.append(window.draw_self())

    def remove_window(self):
        self.__windows.pop()
        self.__windows_matrices.pop()

    def step(self, action):
        if type(action) is not np.ndarray:
            raise InvalidActionError('Invalid Action')

        new_window = False
        reward = 0
        window = None
        close_window = False
        need_redraw = False
        close_non_modal = False
        for i in range(-1, -len(self.__windows) - 1, -1):
            reward, includes_point, matrix_self, abs_coords, need_redraw, new_window, window, close_window = self.__windows[i].click(action, self.__windows[i].relative_coordinates)
            print(reward)
            if includes_point:
                self.__windows_matrices[i] = MatrixUtils.blit_image(self.__windows_matrices[i], matrix_self,
                                                                    abs_coords - self.__windows[i].relative_coordinates)
                self.__current_matrix = MatrixUtils.blit_image(self.__current_matrix, matrix_self, abs_coords)
                if need_redraw:
                    self.__windows_matrices[i] = self.__windows[i].draw_self()
                break
            else:
                if self.__windows[i].modal:
                    break
                else:
                    if not MatrixUtils.includes_point(action, self.__windows[i].relative_coordinates, self.__windows[i].width, self.__windows[i].height):
                        close_non_modal = True
        if new_window:
            self.add_window(window)
        if close_window or close_non_modal:
            self.__windows[-1].reset()
            self.remove_window()
            self.__windows[-1].reset()
            self.__windows_matrices[-1] = self.__windows[-1].draw_self()
        if need_redraw or new_window or close_window or close_non_modal:
            self.__current_matrix = self.stack_windows()
        return self.__current_matrix, reward

    def stack_windows(self) -> np.ndarray:
        coo = np.array([0, 0])
        final = self.__windows_matrices[0]
        for k in range(1, len(self.__windows_matrices)):
            coo = coo + self.__windows[k].relative_coordinates
            final = MatrixUtils.blit_image(final, self.__windows_matrices[k], coo)
        return final

    def reset(self):
        pass

    def close(self):
        pass


