from interface import Interface
from typing import List


class Vertex:
    def __init__(self, key: any, payload: any):
        self.key = key
        self.payload = payload


class Graph(Interface):
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
