from typing import List
from Graphs.graph import Graph, Vertex


class AdjacencyMatrix(Graph):
    def __init__(self, vertices: int):
        self.vertices = [[10 for y in range(vertices)] for x in range(vertices)]

    # requires adding an extra column to each row and an extra row to represent the new vertex
    def add_vertex(self, vertex: Vertex) -> None:
        pass

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int) -> None:
        pass

    def get_vertex(self, vertex_key: any) -> Vertex:
        pass

    def get_vertices(self) -> List[Vertex]:
        pass

    def __contains__(self, item: Vertex) -> bool:
        pass

    def __str__(self):
        largest_vertex_string_length = 1 + len(str(len(self.vertices) - 1))
        rep = ' ' * largest_vertex_string_length
        for index, item in enumerate(self.vertices):
            header_length = len('V' + str(index))
            grid_length = len(item[0].__str__()) + 1
            separator = ' ' * (grid_length)
            rep += '{}V{}'.format(separator, index)
        rep += '\n'
        for index, vertex in enumerate(self.vertices):
            rep += 'V{}{}'.format(index, ' ' * (largest_vertex_string_length - len('V' + str(index))))
            for edge in vertex:
                rep += '{}{}'.format(' ' * (largest_vertex_string_length + len(edge.__str__())), edge)
            rep += '\n'
        return rep


if __name__ == '__main__':
    adjacency_matrix = AdjacencyMatrix(20)
    print(adjacency_matrix)
