import numpy as np

from model.linalg.linalg_object import LinalgObject


class Vector(LinalgObject):
    def cross(self, vector):
        ar = np.cross(self.coords, vector.coords)
        return Vector(ar)

    def normalize(self):
        n = np.linalg.norm(self.coords)
        return Vector(self.coords / n)

    def scale(self, r):
        return Vector(self.coords * r)

    def dot(self, vector):
        return np.dot(self.coords, vector.coords)

    def orthogonal(self):
        x, y, z = tuple(self.coords)
        # Drehtrick
        return Vector(-z, y, x)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scale(other)

    def __add__(self, other):
        ar = np.add(self.coords, other.coords)
        return Vector(ar)

    def __sub__(self, other):
        ar = np.subtract(self.coords, other.coords)
        return Vector(ar)

    def __repr__(self):
        return "Vector" + super().__repr__()

    def __iter__(self):
        for a in self.coords:
            yield a
