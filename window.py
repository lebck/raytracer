import time
import timeit

import numpy as np

from PIL import Image

from model import World

if __name__ == '__main__':

    start = timeit.default_timer()

    WIDTH = 1280//3
    HEIGHT = 720//3

    world = World.get_standard_world()

    pixels = world.camera.create_img(WIDTH, HEIGHT)

    Image.fromarray(pixels).show()

    stop = timeit.default_timer()

    print("Run time:", start-stop)
