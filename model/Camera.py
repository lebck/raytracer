import math

import numpy as np

from model.Ray import Ray
from model.linalg.Point import Point
from model.linalg.Vector import Vector
from model.objects.Color import ColorHelper
from model.objects.Plane import Plane

BACKGROUND_COLOR = (255, 255, 255)
DIST = 750


class Camera:
    """Kamera - Erzeugt das Bild und erhält Kamera-Parameter"""
    def __init__(self, e: Point, c: Point, up: Vector, fov, world):
        self.world = world
        self.fov = fov
        self.up = up
        self.c = c
        self.e = e

        self.f = (c - e).normalize()
        self.s = self.f.cross(self.up).normalize()
        self.u = self.s.cross(self.f)

        self.RATIO = 16/9

    def _get_ray(self, x, y, p_width, p_height, width, height):
        """Erzeuge Ray aus gegebenen x/y Koordinaten, Höhe, Breite und Pixelhöhe/-breite"""
        xv = self.s.scale(x * p_width - width / 2)
        yv = self.u.scale(y * p_height - height / 2)

        ray = Ray(self.e, self.f + xv + yv)

        return ray

    def create_img(self, window_width, window_height):
        """Erzeuge das Bild als 2D- Liste von RGB-Werten"""

        # Erzeuge "Leinwand"
        height = 2 * math.tan(self.fov)
        width = self.RATIO * height

        # Berechne Höhe/Breite eines Pixels in Koordinationsystem-Einheiten
        p_width = width / (window_width - 1)
        p_height = height / (window_height - 1)

        color_helper = ColorHelper(self.world.objects, self.world.sun)

        image = np.empty((window_height, window_width, 3), dtype=np.uint8)

        # Erzeuge Bild von oben links nach unten rechts
        for y in range(window_height):

            for x in range(window_width):

                ray = self._get_ray(x, y, p_width, p_height, width, height)
                color = BACKGROUND_COLOR
                maxdist = float('inf')

                # Berechne Kollision des Strahls mit den Objekten in der Welt
                for object in self.world.objects:
                    hitdist = object.intersect(ray)

                    if hitdist and hitdist < maxdist:
                        maxdist = hitdist

                        p = ray.origin + ray.direction.scale(hitdist)

                        color = object.color_at(ray, p, color_helper)

                r, g, b = np.uint8(color[0]), np.uint8(color[1]), np.uint8(color[2])

                img_y = window_height - 1 - y

                image[img_y][x][0] = r
                image[img_y][x][1] = g
                image[img_y][x][2] = b



        return image
