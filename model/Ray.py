from model.linalg.Point import Point
from model.linalg.Vector import Vector


class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self.direction = direction.normalize()
        self.origin = origin

    def __repr__(self):
        return "Ray(%s %s)" % (self.origin, self.direction)

