import timeit

from PIL import Image

from model import world

if __name__ == '__main__':
    start = timeit.default_timer()

    WIDTH = 300
    HEIGHT = 300

    world = world.get_standard_world()

    print("Rendering Image (%sx%s)" % (WIDTH, HEIGHT))

    pixels = world.camera.create_img(WIDTH, HEIGHT)

    Image.fromarray(pixels, 'RGB').show()

    stop = timeit.default_timer()

    print("Finished")
    print("Run time: %ss" % round((stop - start), 1))
