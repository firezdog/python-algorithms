""" Java representation calls for an array of bags of integers, where array indexes correspond to vertices.
Flexibility of Python allows us to replace bags with arrays.
Note that whether we use a bag or list, the API doesn't prevent duplicate (parallel) edges by default.
For the above reason, I use sets instead of lists. """
from typing import Set

from Graphs.Implementations.Graph import Graph


class AdjacencyList(Graph):
    def __init__(self, num_vertices):
        self.vertices = [set() for x in range(num_vertices)]
        self.edges = set()

    def get_num_vertices(self) -> int:
        return len(self.vertices)

    # edge case (no pun intended) -- two list entries added for each edge, except between vertex and itself
    # see below @ add_edge()
    def get_num_edges(self) -> int:
        return len(self.edges)

    def get_edges(self) -> Set[Set[int]]:
        return self.edges

    def get_adjacent(self, vertex) -> Set[int]:
        return self.vertices[vertex]

    def add_edge(self, from_vertex, to_vertex, **kwargs) -> None:
        if from_vertex == to_vertex:    # don't allow self-loops
            return
        edge = frozenset({from_vertex, to_vertex})
        self.edges.add(edge)
        self.vertices[from_vertex].add(to_vertex)
        self.vertices[to_vertex].add(from_vertex)
