from interface import implements
from typing import List
from Graphs.graph import Graph, Vertex


class AdjacencyMatrix(implements(Graph)):
    def __init__(self, vertices: int):
        self.vertices = [[False for y in range(vertices)] for x in range(vertices)]

    # requires recreating the entire matrix with the extra vertex!
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
        rep = '{:3}'.format('')
        for index, _ in enumerate(self.vertices):
            rep += '{:3}V{}'.format('', index)
        rep += '\n'
        for index, vertex in enumerate(self.vertices):
            rep += 'V{}'.format(index)
            for edge in vertex:
                rep += '{:4}{}'.format('', int(edge))
            rep += '\n'
        return rep


if __name__ == '__main__':
    adjacency_matrix = AdjacencyMatrix(10)
    print(adjacency_matrix)
