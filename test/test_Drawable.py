import unittest
from unittest import TestCase
import numpy as np
from PIL import Image

from src.ui.Button import Button


class MyTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        pic_main = Image.open('C:/Users/Ildeniz/Desktop/PRAKTIKUM/Screenshots/window.png').convert('RGB')
        cls.array_window = np.transpose(np.array(pic_main), (1, 0, 2))
        pic_window2 = Image.open('C:/Users/Ildeniz/Desktop/PRAKTIKUM/Screenshots/window2.png').convert('RGB')
        cls.array_window2 = np.transpose(np.array(pic_window2), (1, 0, 2))
        pic_unclicked = Image.open('C:/Users/Ildeniz/Desktop/PRAKTIKUM/Screenshots/button_unclicked.png').convert('RGB')
        cls.array_unclicked = np.transpose(np.array(pic_unclicked), (1, 0, 2))
        pic_clicked = Image.open('C:/Users/Ildeniz/Desktop/PRAKTIKUM/Screenshots/button_clicked.png').convert('RGB')
        cls.array_clicked = np.transpose(np.array(pic_clicked), (1, 0, 2))

    def setUp(self):
        self.button1 = Button(self.array_clicked, self.array_unclicked, self.array_clicked, 2, lambda: True, np.array([0, 0]))

    def test_drawable_size(self):
        self.assertEqual(self.button1.height, self.array_unclicked.shape[1])
        self.assertEqual(self.button1.width, self.array_unclicked.shape[0])

    def test_draw_self(self):
        matrix = self.button1.draw_self(np.array([0, 0]), np.zeros((23, 22, 3)))
        self.assertEqual((matrix == self.array_unclicked).all(), True)

    def test_click(self):
        (reward, includes_point, new_matrix, abs_coords, need_redraw) = self.button1.click(np.array([5, 5]), np.array([0, 0]))
        self.assertFalse(need_redraw)
        self.assertTrue(includes_point)
        self.assertEqual(reward, self.button1.reward)
        self.assertEqual((new_matrix == self.button1.matrix_clicked).all(), True)
        self.assertEqual((abs_coords == np.array([0, 0])).all(), True)


if __name__ == '__main__':
    unittest.main()
