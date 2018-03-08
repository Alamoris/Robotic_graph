class Graph:
    def __init__(self):
        self.adj_array = [[0][0]]
        self.vertex_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def add_vertex(self, vertex_name):
        if vertex_name in self.vertex_dict:
            print("Error graph already have this item")
        else:
            #
            self.vertex_dict.update({vertex_name: (len(self.vertex_dict) + 1)})



    def del_vertex(self, vertex_name):
        if vertex_name in self.vertex_dict:
            pop_value = self.vertex_dict.pop(vertex_name)
            keys = self.vertex_dict.keys()
            for x in keys:
                if self.vertex_dict[x] > pop_value:
                    temp_value = self.vertex_dict[x]
                    self.vertex_dict[x] = pop_value
                    pop_value = temp_value
        else:
            print("Nonexistent value")

    def print(self):
        print(self.vertex_dict)

gra = Graph()
gra.add_vertex('a')
gra.del_vertex('b')
gra.print()
