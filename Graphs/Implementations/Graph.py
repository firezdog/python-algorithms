from abc import ABC, abstractmethod
from typing import Set

import networkx as nx
import matplotlib.pyplot as plt


class Graph(ABC):
    @abstractmethod
    def get_num_vertices(self) -> int:
        pass

    @abstractmethod
    def get_edges(self) -> Set[Set[int]]:
        pass

    @abstractmethod
    def get_num_edges(self) -> int:
        pass

    @abstractmethod
    def get_adjacent(self, vertex) -> Set[int]:
        pass

    @abstractmethod
    def add_edge(self, from_vertex, to_vertex, **kwargs):
        pass


def show_graph(graph: Graph) -> None:
    """ wrapper for module that builds and visualizes a standard graph """
    display_graph = nx.Graph()
    for vertex in range(graph.get_num_vertices()):
        display_graph.add_node(vertex)
    for edge in graph.get_edges():
        edge_list = [x for x in edge]
        # for self loops
        if len(edge_list) == 1:
            edge_list.append(edge_list[0])
        display_graph.add_edge(edge_list[0], edge_list[1])
    nx.draw_circular(display_graph, node_size=400)
    nx.draw_networkx_labels(display_graph, font_size=16, font_color='white', pos=nx.circular_layout(display_graph))
    plt.show()
