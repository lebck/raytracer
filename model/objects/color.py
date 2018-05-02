from model.linalg.vector import Vector
from model.ray import Ray

COLORS = {
    'black': Vector(0, 0, 0)
}

BACKGROUND_COLOR = Vector(0, 0, 0)

CA = Vector(0.3, 0.3, 0.1)

KA = 0.2
KD = 0.9
KS = 0.1

N = 2

REC_DEPTH = 1

KR = 0.8

CHECK_SIZE = 1

BASE_COLOR = Vector(0, 0, 0)
OTHER_COLOR = Vector(1, 1, 1)


class ColorHelper:
    def __init__(self, objects, sun):
        self.objects = objects
        self.sun = sun

    def reflect(self, p, d, n, depth=0):
        dr = d - (n * (n * d)) * 2

        ray = Ray(p, dr)

        for o in self.objects:
            param = o.intersect(ray)

            if param and param > 0.01:
                p2 = p + dr * param

                return o.color_at(ray, p2, self, depth=depth + 1)

        return None

    def checkerboard(self, p):
        v = Vector(p.coords)
        v.scale(1 / CHECK_SIZE)

        x, y, z = v.coords

        if (int(abs(x) + 0.5) + int(abs(y) + 0.5) + int(abs(z) + 0.5)) % 2:
            return OTHER_COLOR
        else:
            return BASE_COLOR

    def phong(self, p, n, d, color, reflection=False, depth=0):

        l = (self.sun - p).normalize()

        lr = l.reflect(n).normalize()

        n = n.normalize()
        d = d.normalize()

        ambient = CA.scale(KA)

        # Schlagschatten
        if self.shadow(p, l):
            color = normalize(ambient)
            return color

        if color == 'checkerboard':
            color = self.checkerboard(p)

        # Reflektion
        if depth < REC_DEPTH and reflection:
            color_r = self.reflect(p, d, n)
            if color_r:
                color = (color * (1 - KR)) + (color_r * KR)

        diffuse = color.scale(KD) * (l * n)
        specular = color.scale(KS) * (lr * d.scale(-1)) ** N

        color = ambient + diffuse + specular

        color = normalize(color)

        return color

    def shadow(self, p, l):
        r = Ray(p, l)

        for o in self.objects:
            param = o.intersect(r)

            if param and param > 0.001:
                return True

        return False


def normalize(x):
    """Nur sinnvolle RGB-Werte akzeptieren"""
    def n(x):
        if 0 <= x <= 1:
            return x
        elif x < 0:
            return 0
        else:
            return 1

    return Vector(*tuple(map(n, x)))


if __name__ == "__main__":
    v1 = Vector(1, 1, 0)

    print(v1.reflect())
