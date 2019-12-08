from abc import ABC, abstractmethod
from collections import Callable
from typing import List, Type, Set

from Graphs.Implementations import Graph


class SearchStrategy(ABC):
    @abstractmethod
    def __init__(self, search, mark: Callable = None, optional_check: Callable = None, immediate=True):
        pass

    @abstractmethod
    def search_graph(self, current_node: int, prev_node: int) -> None:
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

    def get_adjacent(self, vertex: int) -> Set[int]:
        """ wrapper for graph method """
        return self.graph.get_adjacent(vertex)

    # use edge_to > -1 in case we have marked all components e.g. with CC strategy
    def has_path_to(self, vertex: int) -> bool:
        return self.edge_to[vertex] > -1

    def path_to(self, vertex: int) -> List[int]:
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

    def mark(self, vertex: int) -> None:
        self.marked[vertex] = True
        self.total_marked += 1

    def is_marked(self, vertex: int) -> bool:
        """ Is a given vertex connected to the source? """
        return self.marked[vertex]

    def count(self) -> int:
        """ How many vertices are connected to the source. """
        return self.total_marked
