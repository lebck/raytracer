import math

from model.linalg.Point import Point
from model.objects.Color import ColorHelper


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

    def color_at(self, ray, p, color_helper: ColorHelper):
        d = ray.direction
        n = self.normal_at(p)

        color = color_helper.phuong(p, n, d)

        return color


