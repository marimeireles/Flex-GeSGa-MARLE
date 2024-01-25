import pygame
import numpy as np
import random


class PygameVisualizer:
    def __init__(
        self,
        env,
        agents,
        resources,
        goals,
        user_colors,
        width=700,
        height=700,
        cell_size=10,
    ):
        pygame.init()
        self.env = env
        self.agents = agents
        self.resources = resources
        self.goals = goals
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.cell_size = cell_size
        self.colors = user_colors or {}

        self.assign_random_colors()

    def assign_random_colors(self):
        for entity in self.agents + self.resources + self.goals:
            if entity.name and entity.name not in self.colors:
                # If the entity has a color set, use it. Otherwise, assign a random color.
                if entity.color is not None:
                    self.colors[entity.name] = entity.color
                else:
                    self.colors[entity.name] = (
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                    )

        # Set a default background color if not already set
        if "background" not in self.colors:
            self.colors["background"] = (255, 255, 255)  # white background

    def draw_grid(self):
        grid_side = self.width // self.cell_size
        self.screen.fill(self.colors["background"])

        # Draw the grid lines
        for y in range(grid_side):
            for x in range(grid_side):
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        for agent in self.agents:
            print(f"agent name {agent.name}")
            print(agent.position)
            x, y = agent.position
            color = self.colors.get(agent.name, (0, 0, 0))  # default to black
            rect = pygame.Rect(
                x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size
            )
            pygame.draw.rect(self.screen, color, rect)

        for resource in self.resources:
            x, y = resource.position
            color = self.colors.get(resource.name, (0, 0, 0))  # default to black
            rect = pygame.Rect(
                x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size
            )
            pygame.draw.rect(self.screen, color, rect)

        for goal in self.goals:
            x, y = goal.position
            color = self.colors.get(goal.name, (0, 0, 0))  # default to black
            rect = pygame.Rect(
                x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size
            )
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()  # Update the full display surface to the screen
