from model.Camera import Camera
from model.objects.Sphere import Sphere
from model.linalg.Point import Point
from model.linalg.Vector import Vector


class World:
    def __init__(self, objects, cam_conf):
        self.objects = objects

        # Kamera erzeugen
        e, c, up, fov = cam_conf
        self.camera = Camera(e, c, up, fov, self)


def get_standard_world():
    """Erzeugt Standard-Welt zum Testen des Raytacers"""
    s = Sphere(Point(0, 0, 10), 1)

    e = Point(0, 0, 0)
    c = Point(0, 0, 1)
    up = Vector(1, 0, 0)
    fov = 0.1

    cam_conf = e, c, up, fov

    standard_world = World([s], cam_conf)

    return standard_world
