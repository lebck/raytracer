import math

from model.linalg.Point import Point

from .Color import phuong





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

    def normal_at(self, p):
        return (p - self.center).normalize()

    def color_at(self, ray, p, sun):
        # TODO Richtige Beleuchtung implementieren

        d = ray.direction
        n = self.normal_at(p)

        l = p - sun

        color = phuong(l, n, d)

        return tuple(color)


