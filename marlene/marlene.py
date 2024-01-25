import functools
import random
import pygame
from copy import copy

import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete

from pettingzoo import ParallelEnv


class Marlene(ParallelEnv):
    def __init__(self):
        super().__init__()

    def reset(self):
        raise NotImplementedError()

    def terminate_game(self):
        raise NotImplementedError()

    def step(self, actions):
        raise NotImplementedError()

    def render(self, steps, env, actions, visualizer):
        while steps > 0:

            observations, rewards, terminations, truncations, infos = env.step(actions)

            # Draw the grid and agents
            visualizer.draw_grid()
            pygame.time.delay(100)

            steps -= 1

            # Check for termination conditions
            if any(terminations.values()):
                terminate_game()
                return

        print("This game has ended because the specified number of steps was reached.")
        return

    # def observation_space(self):
    #     raise NotImplementedError()

    # def action_space(self):
    #     raise NotImplementedError()