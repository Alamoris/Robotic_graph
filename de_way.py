import sys

import numpy as np
from PIL import Image

import graph_class as gr

MAP_ARRAY = np.zeros((8, 8), dtype=int)
OBSTACLES = [(3, 1), (4, 1), (5, 1), (6, 1), (2, 4), (2, 5),
             (2, 6), (2, 7), (5, 4), (6, 4), (7, 4), (6, 6), (6, 7), (0, 7), (1, 7), (7, 1)]

# Labyrinth test
# OBSTACLES = [(7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 6),
#              (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (5, 3), (4, 3), (3, 3), (3, 4)]
graph = gr.Graph()
# Create bitmap image
img = Image.new( 'RGB', (320, 320), "white")  # create a new black image
pixels = img.load()  # create the pixel map


def fill_map(x_coords, y_coords, color):
    for x in range(40):
        for i in range(40):
            pixels[(40 * x_coords) + x, (40 * y_coords) + i] = color


def expansion_algorithm(start_point, finish_point):
    """
    Main function realisation expansion algorithm
    Take start point and finish pint in tuple format
    """
    def markup_func(start, finish):
        """
        Markup way map
        """

        def alternative_step(cell, step_num):
            storage_array = []
            connections = graph.take_conn(cell)
            for con in connections:
                weight = graph.take_weight(cell, con)
                if weight == 1:
                    cell_x = (con - 1) // 8
                    cell_y = (con - 1) % 8
                    MAP_ARRAY[cell_x, cell_y] = step_num - 9
                    graph.create_conn(cell, con, step_num)
                    storage_array.append(con)
            return storage_array

        def step(cell, step_num, usable_array):
            """
            Calculate one step of expansion algorithm
            """
            cell_x = cell[0]
            cell_y = cell[1]

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

        current_array = []
        custody_array = []
        step_value = 10
        map_size = len(MAP_ARRAY)

        # Initialise first step
        #MAP_ARRAY[start[0]][start[1]] = -9
        # step(start, step_value, first_wave_array)
        current_array = alternative_step(start, step_value)
        # print("first array = {0}, \n second array = {1}".format(current_array, custody_array))
        while True:
            step_value += 1

            # if (step_value % 2) == 1:
            #     current_array = first_wave_array
            #     custody_array = second_wave_array
            # else:
            #     current_array = second_wave_array
            #     custody_array = first_wave_array

            # print(current_array)
            for x in current_array:
                cell_connections_array = alternative_step(x, step_value)
                # step(x, step_value, custody_array)
                custody_array = custody_array + cell_connections_array
                #print(custody_array)

            current_array = custody_array.copy()
            custody_array.clear()

            if finish in current_array:
                for x in current_array:
                    cell_connections_array = alternative_step(x, step_value)
                # print("first array = {1}, \n second array = {0}".format(first_wave_array, second_wave_array))
                break
        return step_value

    def find_de_way(start_point, finish_point, step_val):  # clack clack clack
        def alternative_search_step(cell, step_num, way_array):
            connections = graph.take_conn(cell)
            for con in connections:
                weight = graph.take_weight(cell, con)
                if weight == step_num:
                    way_array.append(con)
                    step_num -= 1
                    return con

        # Searching next station of way
        def search_step(cell, step_num, way_array):
            cell_x = cell[0]
            cell_y = cell[1]
            print(cell_x)
            print(cell_y)

            if cell_x - 1 != -1:
                next_cell = MAP_ARRAY[cell_x - 1][cell_y]
                if next_cell == step_num - 1:
                    way_array.append((cell_x - 1, cell_y))
                    step_num -= 1
                    return (cell_x - 1, cell_y), step_num
                elif next_cell == -9:
                    way_array.append((cell_x - 1, cell_y))
                    return (cell_x - 1, cell_y), step_num

            if cell_y - 1 != -1:
                next_cell = MAP_ARRAY[cell_x][cell_y - 1]
                if next_cell == step_num - 1:
                    way_array.append((cell_x, cell_y - 1))
                    step_num -= 1
                    return (cell_x, cell_y - 1), step_num
                elif next_cell == -9:
                    way_array.append((cell_x, cell_y - 1))
                    return (cell_x, cell_y - 1), step_num

            if cell_x + 1 < map_size:
                next_cell = MAP_ARRAY[cell_x + 1][cell_y]
                if next_cell == step_num - 1:
                    way_array.append((cell_x + 1, cell_y))
                    step_num -= 1
                    return (cell_x + 1, cell_y), step_num
                elif next_cell == -9:
                    way_array.append((cell_x + 1, cell_y))
                    return (cell_x + 1, cell_y), step_num

            if cell_y + 1 < map_size:
                next_cell = MAP_ARRAY[cell_x][cell_y + 1]
                if next_cell == step_num - 1:
                    way_array.append((cell_x, cell_y + 1))
                    step_num -= 1
                    return (cell_x, cell_y + 1), step_num
                elif next_cell == -9:
                    way_array.append((cell_x, cell_y + 1))
                    return (cell_x, cell_y + 1), step_num

        de_way = [finish_point]
        step_value = step_val
        current_cell = finish_point
        map_size = len(MAP_ARRAY)
        i = 0
        while True:
            i += 1

            # work_cell, value = search_step(current_cell, step_value, de_way)
            work_cell = alternative_search_step(current_cell, step_value, de_way)
            current_cell = work_cell
            step_value -= 1

            if current_cell == start_point:
                return de_way

    start_point = start_point[0] * 8 + (start_point[1] + 1)
    finish_point = finish_point[0] * 8 + (finish_point[1] + 1)
    de_way_len = markup_func(start_point, finish_point)
    print(de_way_len)
    way = find_de_way(start_point, finish_point, de_way_len)
    print('Now you know de way!!!')
    way.reverse()
    return way


def dejkstra_algorithm(start_point, finish_point):
    def take_de_dejkstra_way(parents, start, finish):
        way = []
        final_point = start[0] * 8 + (start[1] + 1) - 1
        way_point = finish[0] * 8 + (finish[1] + 1) - 1
        way.append(way_point)
        while True:
            prev_point = parents[way_point]
            if way_point == final_point:
                return way
            way.append(prev_point)
            way_point = prev_point


    parents_array = np.zeros(64, dtype=int)
    weight_array = np.zeros(64, dtype=int)
    for x in range(64):
        weight_array[x] = 99
    passed_point = []
    point_amount = 64 - len(OBSTACLES)

    current_point = start_point[0] * 8 + (start_point[1] + 1)
    weight_array[current_point - 1] = 0
    parents_array[current_point - 1] = current_point - 1
    working_array = graph.take_conn(current_point)

    while True:
        # print(f"working array {working_array}")
        for x in working_array:
            weight = graph.take_weight(current_point, x)
            if weight + weight_array[current_point - 1] < weight_array[x - 1]:
                weight_array[x - 1] = weight + weight_array[current_point - 1]
                parents_array[x - 1] = current_point - 1
                # print(f"coords {x % 8} : {x // 8}")
                MAP_ARRAY[(x - 1) // 8][(x - 1) % 8] = weight + weight_array[current_point - 1]
        passed_point.append(current_point)
        # print(f"weight array\n{weight_array}")

        if len(passed_point) == point_amount:
            break

        min_weight = max(weight_array) + 1
        next_point = 0
        for x in range(len(weight_array) - 1):
            weight = weight_array[x]
            if weight != 0:
                if min_weight > weight:
                    if x + 1 in passed_point:
                        ...
                    else:
                        min_weight = weight
                        next_point = x + 1

        current_point = next_point
        # print(f"cur point now = {current_point}")
        working_array = graph.take_conn(current_point)
    finith_way = take_de_dejkstra_way(parents_array, start_point, finish_point)
    finith_way.reverse()
    return finith_way

def initialize_graph():
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
                    graph.create_conn((x * 8 + (i + 1)), (x * 8 + (i + 1) + 1), 1)

            if cords in OBSTACLES or (x + 1, i) in OBSTACLES:
                ...
            else:
                if x != 7:
                    graph.create_conn((x * 8 + (i + 1)), ((x + 1) * 8 + (i + 1)), 1)


def convert(treatment):
    return [((x - 1) // 8, (x - 1) % 8) for x in treatment]


def main():
    #graph.create_conn(58, 57, 10)
    #wayp = dejkstra_algorithm((7, 0), (7, 7))
    #de_way = []
    #for x in wayp:
    #    de_way.append((x // 8, x % 8))
    #print(de_way)
    initialize_graph()


    de_way = expansion_algorithm((7, 0), (7, 7))
    de_way = convert(de_way)
    print(de_way)

    # Paint way to map
    for x in de_way:
        fill_map(int(x[1]), int(x[0]), (0, 200, 0))

    #de_way = dict(de_way)
    # Painting map
    for x in range(8):
        for i in range(8):
            if graph.check_empty(x * 8 + (i + 1)):
                fill_map(i, x, (0, 0, 0))

    for x in MAP_ARRAY:
        print(x)
    img.show()
    # graph.print_func()

if __name__ == "__main__":
    print("Включение алгоритма поиска пути")
    sys.exit(main())