from model.objects.world_object import WorldObject


class Plane(WorldObject):
    def __init__(self, point, normal, color, reflection):
        super().__init__(color, reflection)
        self.point = point
        self.normal = normal

    def __repr__(self):
        return "Plane(%s %s)" % (self.point, self.normal)

    def intersect(self, ray):
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)

        if b:
            return - a / b

    def normal_at(self, p):
        return self.normal

    def color_at(self, ray, p, color_helper, depth=0):
        return color_helper.phong(p, self.normal, ray.direction, self.color, reflection=self.reflection, depth=depth)
