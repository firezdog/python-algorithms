from abc import ABC, abstractmethod
from typing import List


class Vertex:
    def __init__(self, key: any, payload: any):
        self.key = key
        self.payload = payload


class Graph(ABC):
    @abstractmethod
    def add_vertex(self, vertex: Vertex) -> None:
        pass

    @abstractmethod
    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: int) -> None:
        pass

    @abstractmethod
    def get_vertex(self, vertex_key: any) -> Vertex:
        pass

    @abstractmethod
    def get_vertices(self) -> List[Vertex]:
        pass

    @abstractmethod
    def __contains__(self, item: Vertex) -> bool:
        pass
