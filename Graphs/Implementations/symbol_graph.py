from typing import Dict, Set, Union, FrozenSet

from Graphs.Implementations.Graph import Graph


class SymbolGraph(Graph):
    def __init__(self):
        self.adjacencies = {}  # type: Dict[str, Set[int]]
        self.vertex_map = {}  # type: Dict[Union[str, int], Union[int, str]]
        self.edges = set()  # type: Set[FrozenSet[int]]
        self.num_edges = 0
        self.num_vertices = 0

    def add_edge(self, from_vertex: str, to_vertex: str, **kwargs):
        if from_vertex == to_vertex:    # no self-loops
            return
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adjacencies[from_vertex].add(self.vertex_map[to_vertex])
        self.adjacencies[to_vertex].add(self.vertex_map[from_vertex])
        self.edges.add(frozenset({self.vertex_map[from_vertex], self.vertex_map[to_vertex]}))

    def add_vertex(self, vertex):
        adjacency = self.adjacencies.get(vertex, None)
        if not adjacency:
            self.adjacencies[vertex] = set()
            self.vertex_map[vertex] = self.num_vertices
            self.vertex_map[self.num_vertices] = vertex
            self.num_vertices += 1

    def get_edges(self):
        return self.edges

    def get_num_edges(self):
        return len(self.edges)

    def get_num_vertices(self):
        return self.num_vertices

    def get_adjacent(self, vertex: Union[str, int]):
        if type(vertex) is int:
            key = self.vertex_map[vertex]
        else:
            key = vertex
        return self.adjacencies[key]
