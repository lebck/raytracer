import numpy as np
from model.linalg.LinalgObject import LinalgObject


class Vector(LinalgObject):
    def cross(self, vector):
        ar = np.cross(self.coords, vector.coords)
        return Vector(ar)

    def normalize(self):
        n = np.linalg.norm(self.get_coords())
        x, y, z = list(np.array(self.get_coords()) / n)
        return Vector(x, y, z)

    def scale(self, r):
        x, y, z = np.array(self.get_coords()) * r
        return Vector(x, y, z)

    def dot(self, vector):
        # print(self.coords(), vector.coords(), np.dot(self.coords(), vector.coords()))
        return np.dot(self.get_coords(), vector.get_coords())

    def orthogonal(self):

        x, y, z = self.get_coords()
        # Drehtrick
        return Vector(-z, y, x)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scale(other)

    def __add__(self, other):
        x, y, z = np.add(self.get_coords(), other.get_coords())
        return Vector(x, y, z)

    def __repr__(self):
        return "Vector" + super().__repr__()

    def __iter__(self):
        for a in self.get_coords():
            yield a


