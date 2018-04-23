import numpy as np

from model.linalg.linalg_object import LinalgObject
from model.linalg.vector import Vector


class Point(LinalgObject):
    def __sub__(self, other):
        ar = self.coords - other.coords

        return Vector(ar)

    def __add__(self, other):
        if isinstance(other, Vector):
            ar1 = self.coords
            ar2 = other.coords

            return Point(np.add(ar1, ar2))

    def __repr__(self):
        return "Point" + super().__repr__()
