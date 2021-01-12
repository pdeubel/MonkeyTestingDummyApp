import numpy as np

from src.Application2 import Application2
import random
import time

env = Application2()

maximum = 0

start_total = time.process_time()

for i in range(0, 100000):
    point = np.array([random.randint(0, env.width - 1), random.randint(0, env.height - 1)])
    start = time.process_time_ns()
    result_matrix, reward = env.step(point)
    tim = time.process_time_ns() - start
    # print(tim)
    if tim > maximum:
        maximum = tim

print(time.process_time() - start_total)
print(maximum)
