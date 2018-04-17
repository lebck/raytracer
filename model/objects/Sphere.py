import math

from model.linalg.Point import Point


class Sphere:
    def __init__(self, center: Point, radius: int):
        self.radius = radius
        self.center = center

    def __repr__(self):
        return "Sphere(%s %s)" % (repr(self.center), self.radius)

    def intersect(self, ray):
        co = self.center - ray.origin
        v = co.dot(ray.direction)

        dis = v*v - co * co + self.radius*self.radius

        if dis > 0:
            return v - math.sqrt(dis)

    def color_at(self, ray):
        # TODO Richtige Beleuchtung implementieren
        return 0, 0, 0
