from Graphs.Graph import Graph


class AdjacencyList(Graph):
    def __init__(self, num_vertices):
        self.vertices = [[] * num_vertices]

    def get_num_vertices(self):
        return len(self.vertices)

    def get_num_edges(self):
        pass

    def get_adjacent(self, vertex):
        pass

    def add_edge(self, from_vertex, to_vertex, weight):
        pass
