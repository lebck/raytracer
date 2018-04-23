import numpy as np

from model.linalg.LinalgObject import LinalgObject
from model.linalg.Vector import Vector


class Point(LinalgObject):
    def __sub__(self, other):
        ar = np.array(self.get_coords()) - np.array(other.get_coords())
        x, y, z = list(ar)

        return Vector(x, y, z)

    def __add__(self, other):
        if isinstance(other, Vector):
            x, y, z = self.get_coords()
            x2, y2, z2 = other.get_coords()
            return Point(x+x2, y+y2, z+z2)

    def __repr__(self):
        return "Point" + super().__repr__()

