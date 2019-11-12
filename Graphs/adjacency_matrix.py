from typing import List
from Graphs.graph import Graph, Vertex


class AdjacencyMatrix(Graph):
    def __init__(self, vertices: List[Vertex]):
        self.cell_size = 6
        self.vertices = vertices
        self.matrix = [[0 for y in range(len(vertices))] for x in range(len(vertices))]

    def set_cell_size(self, cell_size: int) -> None:
        self.cell_size = cell_size

    # requires adding an extra column to each row and an extra row to represent the new vertex
    def add_vertex(self, vertex: Vertex) -> None:
        pass

    # easy mode for matrix: assume / require the keys are integers corr. to array position, otherwise we'd search
    def add_edge(self, from_vertex: int, to_vertex: int, weight: int) -> None:
        self.matrix[from_vertex][to_vertex] = weight
        self.matrix[to_vertex][from_vertex] = weight

    # by key
    def get_vertex(self, vertex_key: any) -> Vertex:
        for vertex in self.vertices:
            if vertex.key == vertex_key:
                return vertex

    def get_vertices(self) -> List[Vertex]:
        vertices = list()
        return self.vertices

    # by key
    def __contains__(self, vertex_key: any) -> bool:
        return self.get_vertex(vertex_key) is not None

    def render(self):
        rep = ' ' * self.cell_size
        for i, row in enumerate(self.matrix):
            col_header = '{}'.format(self.vertices[i])
            rep += '{}{}'.format(col_header, ' ' * (self.cell_size - len(col_header)))
        rep += '\n'
        for i, row in enumerate(self.matrix):
            row_header = '{}'.format(self.vertices[i])
            rep += '{}{}'.format(row_header, ' ' * (self.cell_size - len(row_header)))
            for edge in row:
                rep += str(edge) + ' ' * (self.cell_size - len(str(edge)))
            rep += '\n'
        print(rep)


if __name__ == '__main__':
    sample_vertices = list()
    for index in range(10):
        new_vertex = Vertex(index, None)
        sample_vertices.append(new_vertex)
    adjacency_matrix = AdjacencyMatrix(sample_vertices)
    adjacency_matrix.add_edge(3, 5, 1)
    adjacency_matrix.add_edge(5, 3, 2)
    adjacency_matrix.add_edge(4, 5, 1)
    adjacency_matrix.render()
    print(adjacency_matrix.get_vertex(3))
    print(4 in adjacency_matrix)
    print(12 in adjacency_matrix)
    print(adjacency_matrix.get_vertices())
