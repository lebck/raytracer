import timeit

from PIL import Image

from model import world

if __name__ == '__main__':
    start = timeit.default_timer()

    WIDTH = 400
    HEIGHT = 400

    world = world.get_standard_world()

    pixels = world.camera.create_img(WIDTH, HEIGHT)

    Image.fromarray(pixels).show()

    stop = timeit.default_timer()

    print("Run time: %s s" % (stop - start))
