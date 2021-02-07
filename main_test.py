from statistics import mean

import numpy as np

from src.Application2 import Application2
import random
import time

env = Application2()
width = env.width - 1
height = env.height - 1


def test_with_stats(num_of_iterations: int):

    start_total = time.process_time()
    frame_times = []

    for i in range(0, num_of_iterations):
        point = np.array([random.randint(0, width), random.randint(0, height)])
        # point = np.array([54, 14])
        # point = np.array([220, 115])
        start = time.process_time()
        result_matrix, reward, _ = env.step(point)
        tim = time.process_time() - start
        frame_times.append(tim * 1000)

    print('Total Time: ' + str(time.process_time() - start_total) + ' sec')
    print('Longest Frame Time: ' + str(max(frame_times)) + ' ms')
    print('Mean Frame Time: ' + str(mean(frame_times)) + ' ms')
    print(env.get_progress())


def test_without_stats(num_of_iterations: int):
    for i in range(0, num_of_iterations):
        point = np.array([random.randint(0, width), random.randint(0, height)])
        result_matrix, reward, _ = env.step(point)


test_with_stats(1000000)
