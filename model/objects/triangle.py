from model.objects.world_object import WorldObject


class Triangle(WorldObject):
    def __init__(self, a, b, c, color, reflection):
        super().__init__(color=color, reflection=reflection)
        self.c = c
        self.b = b
        self.a = a

        self.u = b - a
        self.v = c - a

        self.normal = self.u.cross(self.v).normalize()

    def __repr__(self):
        return "Triangle(%s %s %s)" % (self.a, self.b, self.c)

    def intersect(self, ray):
        w = ray.origin - self.a
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)

        if dvu == 0.0:
            return None

        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu

        if 0 <= r <= 1 and 0 <= s <= 1 and r + s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normal_at(self, p):
        return self.normal

    def color_at(self, ray, p, color_helper, depth=0):
        return color_helper.phong(p, self.normal, ray.direction, self.color, reflection=self.reflection, depth=depth)
