from typing import Optional, Tuple


class Agent:
    # Example usage:
    # agent = Agent(position=(1, 2), name="AgentName", color=(255, 255, 255))
    def __init__(
        self,
        position: Tuple[int, int],
        name: Optional[str] = None,
        color: Optional[Tuple[int, int, int]] = None,
    ):
        self.name = name
        self.color = color
        self.position = position

    @property
    def observation_space(self):
        raise NotImplementedError(
            "The observation_space must be defined by the subclass."
        )

    @property
    def action_space(self):
        raise NotImplementedError("The action_space must be defined by the subclass.")

    def __str__(self):
        return f"<{type(self).__name__} instance at {self.position} color {self.color}>"

    def set_color(self, new_color: str):
        self.color = new_color
