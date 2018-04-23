from model.Ray import Ray
from model.linalg.Vector import Vector

CA = Vector(0, 250, 250)
CIN = Vector(255, 255, 255)

KA = 0.3
KD = 0.4
KS = 0.5

N = 2


class ColorHelper:
    def __init__(self, objects, sun):
        self.objects = objects
        self.sun = sun

    def phuong(self, p, n, d):
        l = (self.sun - p).normalize()

        lr = l.orthogonal().normalize()

        n = n.normalize()
        d = d.normalize()

        ambient = CA.scale(KA)

        if self.shadow(p, l):
            return list(map(normalize, ambient))

        diffuse = CIN.scale(KD) * (l * n)
        specular = CIN.scale(KS) * (lr * d.scale(-1)) ** N

        color = ambient + diffuse + specular

        # print(ambient, diffuse, specular)

        color = list(map(normalize, color))

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
    if 0 <= x <= 255:
        return x
    elif x < 0:
        return 0
    else:
        return 255







if __name__ == "__main__":
    v1 = Vector(1, 1, 0)

    print(v1.orthogonal())
