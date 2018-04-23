from model.linalg.vector import Vector
from .color import COLORS


class WorldObject:
    def __init__(self, color=COLORS['black'], reflection=False):
        self.reflection = reflection

        if isinstance(color, str):
            self.color = color
        else:
            x, y, z = color
            self.color = Vector(x, y, z)
