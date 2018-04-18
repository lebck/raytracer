import math

from model.Camera import Camera
from model.objects.Sphere import Sphere
from model.linalg.Point import Point
from model.linalg.Vector import Vector


class World:
    def __init__(self, objects, cam_conf, sun):
        self.objects = objects

        # Kamera erzeugen
        e, c, up, fov = cam_conf
        self.camera = Camera(e, c, up, fov, self)

        self.sun = sun


def get_standard_world():
    """Erzeugt Standard-Welt zum Testen des Raytacers"""
    s = Sphere(Point(0, 0, 3), 1)

    e = Point(0, 0, 0)
    c = Point(0, 0, 1)
    up = Vector(1, 0, 0)
    fov = math.pi/4

    cam_conf = e, c, up, fov

    sun = Point(10, 10, 10)

    standard_world = World([s], cam_conf, sun)

    return standard_world
