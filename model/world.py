import math

from model.camera import Camera
from model.linalg.point import Point
from model.linalg.vector import Vector
from model.objects.plane import Plane
from model.objects.sphere import Sphere
from model.objects.triangle import Triangle


class World:
    def __init__(self, objects, cam_conf, sun):
        self.objects = objects

        # Kamera erzeugen
        e, c, up, fov = cam_conf
        self.camera = Camera(e, c, up, fov, self)

        self.sun = sun


def get_standard_world():
    """Erzeugt Standard-Welt zum Testen des Raytracers"""
    # -- Objekte erzeugen
    s = Sphere(Point(-1, 1.5, 3), 1, (1, 0, 0), True)
    s2 = Sphere(Point(-1, -1.5, 3), 1, (0, 1, 0), True)
    s3 = Sphere(Point(1.5, 0, 3), 1, (0, 0, 1), True)
    p = Plane(Point(-3, 0, 0), Vector(1, 0, 0), 'checkerboard', True)
    t = Triangle(Point(-1, 1.5, 4), Point(-1, -1.5, 4), Point(1.5, 0, 4), (0.5, 0.5, 0), False)

    objs = [t, p, s, s2, s3]
    # --

    # -- Kamera-Parameter erzeugen
    e = Point(0, 0, -5)
    c = Point(0, 0, 1)
    up = Vector(1, 0, 0)
    fov = math.pi / 8

    cam_conf = e, c, up, fov
    # --

    # Sonne
    sun = Point(5, 0, 0)

    standard_world = World(objs, cam_conf, sun)

    return standard_world
