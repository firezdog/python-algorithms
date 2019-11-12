from typing import List
from Graphs.graph import Graph, Vertex


class AdjacencyMatrix(Graph):
    def __init__(self, vertices: int):
        self.cell_size = 6
        self.vertices = [[False for y in range(vertices)] for x in range(vertices)]

    def set_cell_size(self, cell_size: int) -> None:
        self.cell_size = cell_size

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
        rep = ' ' * self.cell_size
        for i, row in enumerate(self.vertices):
            col_header = 'V{}'.format(i)
            rep += '{}{}'.format(col_header, ' ' * (self.cell_size - len(col_header)))
        rep += '\n'
        for i, row in enumerate(self.vertices):
            row_header = 'V{}'.format(i)
            rep += '{}{}'.format(row_header, ' ' * (self.cell_size - len(row_header)))
            for edge in row:
                rep += str(edge) + ' ' * (self.cell_size - len(str(edge)))
            rep += '\n'
        return rep


if __name__ == '__main__':
    adjacency_matrix = AdjacencyMatrix(5)
    adjacency_matrix.set_cell_size(10)
    print(adjacency_matrix)
