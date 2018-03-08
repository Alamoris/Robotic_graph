import numpy as np


class Graph:
    def __init__(self):
        self.adj_array = [[0, 1, 1, 0], [0, 1, 0, 1], [1, 0, 0, 0], [1, 1, 1, 0]]
        self.vertex_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def add_vertex(self, vertex_name):
        if vertex_name in self.vertex_dict:
            print("Error graph already have this item")
        else:
            # Add dict value with new vertex
            self.vertex_dict.update({vertex_name: (len(self.vertex_dict) + 1)})

            # Add vertex from map array
            self.adj_array.append([])
            for x in self.adj_array:
                if self.adj_array[len(self.adj_array) - 1] == x:
                    for i in range(len(self.vertex_dict) - 1):
                        x.append(0)
                x.append(0)

    def del_vertex(self, vertex_name):
        if vertex_name in self.vertex_dict:
            row_to_delete = self.vertex_dict[vertex_name] - 1

            # Del some vertex from dict and shifting it
            pop_value = self.vertex_dict.pop(vertex_name)
            keys = self.vertex_dict.keys()
            for x in keys:
                if self.vertex_dict[x] > pop_value:
                    temp_value = self.vertex_dict[x]
                    self.vertex_dict[x] = pop_value
                    pop_value = temp_value

            # Del some vertex from map array and shifting it
            self.adj_array.pop(row_to_delete)
            for x in self.adj_array:
                # Realisation without directly pop
                for i in range(row_to_delete, len(self.vertex_dict)):
                    x[i] = x[i+1]
                x.pop()

                # Realisation with directly pop
                # x.pop(row_to_delete)

        else:
            print("Nonexistent value")

    def print(self):
        print(f"Значение словаря вершин {self.vertex_dict}")
        for x in self.adj_array:
            print(x)


gra = Graph()
gra.print()
gra.del_vertex('b')
gra.print()
