from typing import Optional, Tuple


class Goal:
    def __init__(
        self,
        position: Tuple[int, int],
        name: Optional[str] = None,
        color: Optional[Tuple[int, int, int]] = None,
    ):
        self.name = name
        self.color = color
        if position is None:
            raise ValueError("Position is mandatory")
        self.position = position

    def __str__(self):
        return f"<{type(self).__name__} instance at {self.position} color {self.color}>"

    def set_color(self, new_color: str):
        self.color = new_color
