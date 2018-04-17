import matplotlib.cm as cm
import numpy as np

from PIL import Image

from model.Camera import Camera
from model import World
from model.linalg.Point import Point
from model.linalg.Vector import Vector

if __name__ == '__main__':

    WIDTH = 1280//3
    HEIGHT = 720//3

    world = World.get_standard_world()

    pixels = world.camera.create_img(WIDTH, HEIGHT)

    Image.fromarray(np.array(pixels).astype('uint8')).show()
