from abc import ABC, abstractmethod
from typing import List, Type

from Graphs.Implementations import Graph


class SearchStrategy(ABC):
    @abstractmethod
    def __init__(self, search):
        pass

    @abstractmethod
    def search_graph(self, waypoint: int) -> None:
        pass


class Search:
    def __init__(self, graph: Graph, source: int, search_strategy: Type[SearchStrategy]):
        self.graph = graph
        self.total_marked = 0
        self.marked = [False] * graph.get_num_vertices()
        self.edge_to = [-1] * graph.get_num_vertices()
        self.edge_to[source] = source
        self.source = source
        self.search_strategy = search_strategy(self)

    def has_path_to(self, vertex: int) -> bool:
        return self.marked[vertex]

    def path_to(self, vertex: int) -> List:
        path = list()
        if self.has_path_to(vertex):
            current_node = vertex
            while current_node != self.source:
                path.append(current_node)
                current_node = self.edge_to[current_node]
            path.append(self.source)
        else:
            print("No path from {} to {}".format(self.source, vertex))
        return path

    def is_marked(self, vertex: int) -> bool:
        """ Is a given vertex connected to the source? """
        return self.marked[vertex]

    def count(self) -> int:
        """ How many vertices are connected to the source. """
        return self.total_marked
