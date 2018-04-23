from model.linalg.vector import Vector
from model.ray import Ray

COLORS = {
    'black': Vector(0, 0, 0)
}

BACKGROUND_COLOR = Vector(255, 255, 255)

CA = Vector(100, 100, 50)

KA = 0.1
KD = 0.5
KS = 0.5

N = 2

REC_DEPTH = 2

KR = 0.3

CHECK_SIZE = 1

BASE_COLOR = Vector(0, 0, 0)
OTHER_COLOR = Vector(255, 255, 255)


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

        return BACKGROUND_COLOR

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

        lr = l.orthogonal().normalize()

        n = n.normalize()
        d = d.normalize()

        ambient = CA.scale(KA)

        # Schlagschatten
        if self.shadow(p, l):
            x, y, z = list(map(normalize, ambient))
            return Vector(x, y, z)

        if color == 'checkerboard':
            color = self.checkerboard(p)

        # Reflektion
        if depth < REC_DEPTH and reflection:
            color_r = self.reflect(p, d, n)

            color = (color * (1 - KR)) + (color_r * KR)

        diffuse = color.scale(KD) * (l * n)
        specular = color.scale(KS) * (lr * d.scale(-1)) ** N

        color = ambient + diffuse + specular

        # print(ambient, diffuse, specular)

        r, g, b = list(map(normalize, color))

        return Vector(r, g, b)

    def shadow(self, p, l):
        r = Ray(p, l)

        for o in self.objects:
            param = o.intersect(r)

            if param and param > 0.001:
                return True

        return False


def normalize(x):
    """Nur sinnvolle RGB-Werte akzeptieren"""
    if 0 <= x <= 255:
        return x
    elif x < 0:
        return 0
    else:
        return 255


if __name__ == "__main__":
    v1 = Vector(1, 1, 0)

    print(v1.orthogonal())
