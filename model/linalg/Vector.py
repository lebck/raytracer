import numpy as np
from model.linalg.LinalgObject import LinalgObject


class Vector(LinalgObject):
    def cross(self, vector):
        x, y, z = list(np.cross(self.coords(), vector.coords()))
        return Vector(x, y, z)

    def normalize(self):
        n = np.linalg.norm(self.coords())
        x, y, z = list(np.array(self.coords()) / n)
        return Vector(x, y, z)

    def scale(self, r):
        x, y, z = np.array(self.coords()) * r
        return Vector(x, y, z)

    def dot(self, vector):
        # print(self.coords(), vector.coords(), np.dot(self.coords(), vector.coords()))
        return np.dot(self.coords(), vector.coords())

    def __mul__(self, other):
        return self.dot(other)

    def __add__(self, other):
        x, y, z = np.add(self.coords(), other.coords())
        return Vector(x, y, z)

    def __repr__(self):
        return "Vector" + super().__repr__()

