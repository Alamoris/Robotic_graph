class Graph:
    def __init__(self):
        self.adj_array = []
        self.vertex_dict = {}

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

    def create_conn(self, x_conn, y_conn):
        id_a = self.vertex_dict[x_conn] - 1
        id_b = self.vertex_dict[y_conn] - 1
        self.adj_array[id_a][id_b] = 1
        self.adj_array[id_b][id_a] = 1

    def check_conn(self, name_a, name_b):
        id_a = self.vertex_dict[name_a] - 1
        id_b = self.vertex_dict[name_b] - 1
        if self.adj_array[id_a][id_b] == 1 and self.adj_array[id_b][id_a] == 1:
            return True
        return False

    def check_empty(self, vertex):
        id_vertex = self.vertex_dict[vertex] - 1
        cheked_vertex = self.adj_array[id_vertex]
        if 1 in cheked_vertex:
            return False
        return True

    def print(self):
        print(f"Значение словаря вершин {self.vertex_dict}")
        for x in self.adj_array:
            print(x)
