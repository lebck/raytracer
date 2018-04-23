from model.objects.Color import ColorHelper


class Plane:
    def __init__(self, point, normal):
        self.point = point
        self.normal = normal

    def __repr__(self):
        return "Plane(%s %s)" % (self.point, self.normal)

    def intersect(self, ray):
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)

        if b:
            t = - a / b
            if t > 0:
                return t

    def normal_at(self, p):
        return self.normal

    def color_at(self, ray, p, color_helper):
        return color_helper.phuong(p, self.normal, ray.direction)
