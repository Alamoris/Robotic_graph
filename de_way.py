import random

import numpy as np
from PIL import Image

import graph_class as gr

MAP_ARRAY = np.zeros((8, 8), dtype=int)
OBSTACLES = [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (2, 4), (2, 5), (2, 6), (2, 7), (5, 4), (6, 4), (7, 4), (6, 6), (6, 7), (0, 7), (1, 7)]

# Labyrinth test
# OBSTACLES = [(7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 6),
# (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 3), (5, 3), (4, 3), (3, 3), (3, 4)]

graph = gr.Graph()
# Create bitmap image
img = Image.new( 'RGB', (320, 320), "white")  # create a new black image
pixels = img.load()  # create the pixel map


def fill_map(x_coords, y_coords):
    for x in range(40):
        for i in range(40):
            pixels[(40 * x_coords) + x, (40 * y_coords) + i] = (0, 0, 0)


def markup_func(start_point, finish_point):
    def step(cell, step_num, usable_array):
        cell_x = cell[0]
        cell_y = cell[1]
        map_size = len(MAP_ARRAY)
        print(cell_x)
        print(cell_y)

        next_cell = MAP_ARRAY[cell_x - 1][cell_y]
        if cell_x - 1 != -1:
            if next_cell == 0:
                MAP_ARRAY[cell_x - 1][cell[1]] = step_num + 1
                usable_array.append((cell_x - 1, cell_y))

        if cell_y - 1 != -1:
            next_cell = MAP_ARRAY[cell_x][cell_y - 1]
            if next_cell == 0:
                MAP_ARRAY[cell_x][cell_y - 1] = step_num + 1
                usable_array.append((cell_x, cell_y - 1))

        if cell_x + 1 < map_size:
            next_cell = MAP_ARRAY[cell_x + 1][cell_y]
            if next_cell == 0:
                MAP_ARRAY[cell_x + 1][cell_y] = step_num + 1
                usable_array.append((cell_x + 1, cell_y))

        if cell_y + 1 < map_size:
            next_cell = MAP_ARRAY[cell_x][cell_y + 1]
            if next_cell == 0:
                MAP_ARRAY[cell_x][cell_y + 1] = step_num + 1
                usable_array.append((cell_x, cell_y + 1))


    first_wave_array = []
    second_wave_array = []
    step_value = 0

    # Initialise first step
    MAP_ARRAY[start_point[0]][start_point[1]] = -9
    step(start_point, step_value, first_wave_array)
    print(f"first array = {first_wave_array}, \n second array = {second_wave_array}")
    while True:

        step_value += 1

        if (step_value % 2) == 1:
            current_array = first_wave_array
            custody_array = second_wave_array
        else:
            current_array = second_wave_array
            custody_array = first_wave_array

        print(current_array)
        for x in current_array:
            step(x, step_value, custody_array)
        current_array.clear()

        if MAP_ARRAY[finish_point[0]][finish_point[1]] != 0:
            print(f"first array = {first_wave_array}, \n second array = {second_wave_array}")
            break


for x in OBSTACLES:
    MAP_ARRAY[x[0], x[1]] = -1

# Generate our graph vertex
for x in range(1, 65):
    graph.add_vertex(x)

# Filling in adjective graph
for x in range(8):
    for i in range(8):
        cords = (x, i)
        if cords in OBSTACLES or (x, i + 1) in OBSTACLES:
            ...
        else:
            if i != 7:
                graph.create_conn((x * 8 + (i + 1)), (x * 8 + (i + 1) + 1))

        if cords in OBSTACLES or (x + 1, i) in OBSTACLES:
            ...
        else:
            if x != 7:
                graph.create_conn((x * 8 + (i + 1)), ((x + 1) * 8 + (i + 1)))

# Painting map
for x in range(8):
    for i in range(8):
        if graph.check_empty(x * 8 + (i + 1)):
            fill_map(i, x)

markup_func((7, 0), (7, 7))

for x in MAP_ARRAY:
    print(x)
graph.print()
img.show()