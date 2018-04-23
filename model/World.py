import math

from model.Camera import Camera
from model.objects.Plane import Plane
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
    """Erzeugt Standard-Welt zum Testen des Raytracers"""
    # -- Objekte erzeugen
    s = Sphere(Point(0, 0, 3), 1)
    p = Plane(Point(-3, 0, 0), Vector(1, 0, 0))
    su = Sphere(Point(1, 1, 3), 1)
    # --

    objs = [s, p]

    # -- Kamera-Parameter erzeugen
    e = Point(0, 0, 0)
    c = Point(0, 0, 1)
    up = Vector(1, 0, 0)
    fov = math.pi/4

    cam_conf = e, c, up, fov
    # --

    # Sonne
    sun = Point(2, 0, 3)

    standard_world = World(objs, cam_conf, sun)

    return standard_world
