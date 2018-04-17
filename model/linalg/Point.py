import numpy as np

from model.linalg.LinalgObject import LinalgObject
from model.linalg.Vector import Vector


class Point(LinalgObject):
    def __sub__(self, other):
        ar = np.array(self.coords()) - np.array(other.coords())
        x, y, z = list(ar)

        return Vector(x, y, z)

    def __repr__(self):
        return "Point" + super().__repr__()

