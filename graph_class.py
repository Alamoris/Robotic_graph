class Graph:
    def __init__(self):
        self.adj_array = []
        self.vertex_dict = {}

    def add_vertex(self, vertex):
        if vertex in self.vertex_dict:
            print("Error graph already have this item")
        else:
            # Add dict value with new vertex
            self.vertex_dict.update({vertex: (len(self.vertex_dict) + 1)})

            # Add vertex from map array
            self.adj_array.append([])
            for x in self.adj_array:
                if self.adj_array[len(self.adj_array) - 1] == x:
                    for i in range(len(self.vertex_dict) - 1):
                        x.append(0)
                x.append(0)

    def del_vertex(self, vertex):
        if vertex in self.vertex_dict:
            row_to_delete = self.vertex_dict[vertex] - 1

            # Del some vertex from dict and shifting it
            pop_value = self.vertex_dict.pop(vertex)
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

    def take_conn(self, vertex):
        """
        Take vertex name and return array with vertex numbers of available connections
        """
        connections_array = []
        vertex_id = self.vertex_dict[vertex] - 1
        search_array = self.adj_array[vertex_id]
        i = 1
        for x in search_array:
            if x != 0:
                connections_array.append(i)
            i += 1
        return connections_array

    def take_weight(self, vertex_x, vertex_y):
        """
        Take vertex names and return weight of connection
        """
        x_id = self.vertex_dict[vertex_x] - 1
        y_id = self.vertex_dict[vertex_y] - 1
        weight = self.adj_array[x_id][y_id]
        return weight

    def create_conn(self, x_conn, y_conn, weight):
        x_id = self.vertex_dict[x_conn] - 1
        y_id = self.vertex_dict[y_conn] - 1
        self.adj_array[x_id][y_id] = weight
        self.adj_array[y_id][x_id] = weight

    def check_conn(self, name_a, name_b):
        id_a = self.vertex_dict[name_a] - 1
        id_b = self.vertex_dict[name_b] - 1
        if self.adj_array[id_a][id_b] == 1 and self.adj_array[id_b][id_a] == 1:
            return True
        return False

    def check_empty(self, vertex):
        id_vertex = self.vertex_dict[vertex] - 1
        cheked_vertex = self.adj_array[id_vertex]
        for x in cheked_vertex:
            if x != 0:
                return False
        return True

    def print_func(self):
        print("Значение словаря вершин {0}".format(self.vertex_dict))
        for x in self.adj_array:
            print(x)
