import random

import numpy as np
from PIL import Image


MAP_ARRAY = np.zeros((8, 8), dtype=int)
OBSTACLES = [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (2, 4), (2, 5),
             (2, 6), (2, 7), (5, 4), (6, 4), (7, 4), (6, 6), (6,7)]


def fill_map(x_coords, y_coords):
    for x in range(40):
        for i in range(40):
            pixels[(40 * x_coords) + x, (40 * y_coords) + i] = (0, 0, 0)


img = Image.new( 'RGB', (320, 320), "white")  # create a new black image
pixels = img.load()  # create the pixel map

for x in OBSTACLES:
    MAP_ARRAY[x[0]][x[1]] = 1
    fill_map(x[0], x[1])

img.show()