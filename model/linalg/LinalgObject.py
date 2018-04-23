import numpy as np


class LinalgObject:
    def __init__(self, x, y: int = None, z: int = None):

        # Entweder mit x, y, z oder direkt als np.array initialisieren
        if isinstance(x, np.ndarray):
            self.coords = x
        else:
            self.coords = np.array((x, y, z))

    def get_coords(self):
        return tuple(self.coords)

    def __repr__(self):
        return "(%s %s %s)" % tuple(self.coords)