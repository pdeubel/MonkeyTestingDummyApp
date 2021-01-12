from src.Application2 import Application2
import pygame
import numpy as np
import random
import time

env = Application2()

pygame.init()
display = pygame.display.set_mode((env.width, env.height))
pygame.surfarray.blit_array(display, env.current_matrix)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        point = np.array([random.randint(0, int(env.width / 6)), random.randint(0, int(env.height / 4))])
        result_matrix, reward = env.step(point)
        # print('Reward: ' + str(reward))
        pygame.surfarray.blit_array(display, result_matrix)
        pygame.display.update()

pygame.quit()
