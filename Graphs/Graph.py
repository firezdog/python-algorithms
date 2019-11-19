from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def get_num_vertices(self):
        pass

    @abstractmethod
    def get_num_edges(self):
        pass

    @abstractmethod
    def get_adjacent(self, vertex):
        pass

    @abstractmethod
    def add_edge(self, from_vertex, to_vertex, **kwargs):
        pass
