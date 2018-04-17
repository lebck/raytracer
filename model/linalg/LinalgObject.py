class LinalgObject:
    def __init__(self, x: int, y: int, z: int):
        self.z = z
        self.y = y
        self.x = x

    def coords(self):
        return self.x, self.y, self.z

    def __repr__(self):
        return "(%s %s %s)" % self.coords()