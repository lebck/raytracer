from model import World
from model.Ray import Ray
from model.linalg.Point import Point
from model.linalg.Vector import Vector


def test1():
    v = Point(1, 2, 3) - Point(0, 0, 0)
    print(v)

    v2 = Vector(1, 0, 0)
    print(v.cross(v2))

    v3 = v2.normalize()
    print(v3)

    print(v3.scale(3))


def test2():
    w = World.get_standard_world()

    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))

    print(w.objects[0].intersect(r))


if __name__ == "__main__":
    test2()

