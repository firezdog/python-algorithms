from abc import ABC, abstractmethod
from typing import List


class Vertex:
    def __init__(self, key: any, payload: any):
        self.key = key
        self.payload = payload
        self.suppress_payload = True

    def set_suppress_key(self, suppress_key: bool) -> None:
        self.suppress_payload = suppress_key

    def set_payload(self, payload: any) -> None:
        self.payload = payload

    def __str__(self):
        return '{}:{}'.format(self.key, self.payload) if not self.suppress_payload \
            else '{}'.format(self.key)

    def __repr__(self):
        return self.__str__()


class Graph(ABC):
    @abstractmethod
    def add_vertex(self, vertex: Vertex) -> None:
        pass

    @abstractmethod
    def add_edge(self, from_vertex: any, to_vertex: any, weight: int) -> None:
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
