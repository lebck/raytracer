import numpy as np

from PIL import Image

from model import World

if __name__ == '__main__':

    WIDTH = 1280//3
    HEIGHT = 720//3

    world = World.get_standard_world()

    pixels = world.camera.create_img(WIDTH, HEIGHT)

    Image.fromarray(pixels).show()
