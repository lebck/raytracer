import math

from model.linalg.point import Point
from model.objects.color import ColorHelper
from model.objects.world_object import WorldObject


class Sphere(WorldObject):
    def __init__(self, center: Point, radius: int, color, reflection):
        super().__init__(color, reflection)
        self.radius = radius
        self.center = center

    def __repr__(self):
        return "Sphere(%s %s)" % (repr(self.center), self.radius)

    def intersect(self, ray):
        co = self.center - ray.origin
        v = co.dot(ray.direction)

        dis = v * v - co * co + self.radius * self.radius

        if dis > 0:
            return v - math.sqrt(dis)

    def normal_at(self, p):
        return (p - self.center).normalize()

    def color_at(self, ray, p, color_helper: ColorHelper, depth=0):
        d = ray.direction
        n = self.normal_at(p)

        color = color_helper.phong(p, n, d, self.color, reflection=self.reflection, depth=depth)

        return color
