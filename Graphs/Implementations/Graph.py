from abc import ABC, abstractmethod
from typing import Set, cast

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
    from Graphs.Implementations.symbol_graph import SymbolGraph
    display_graph = nx.Graph()
    for vertex in range(graph.get_num_vertices()):
        display_graph.add_node(vertex)
    for edge in graph.get_edges():
        edge_list = [x for x in edge]
        # for self loops -- this should no longer be a problem since I added checks to eliminate
        if len(edge_list) == 1:
            edge_list.append(edge_list[0])
        display_graph.add_edge(edge_list[0], edge_list[1])
    if isinstance(graph, SymbolGraph):
        display_graph = nx.relabel_nodes(display_graph, graph.vertex_map)
    pos = nx.circular_layout(display_graph)
    custom_pos = {}
    for k, v in pos.items():
        custom_pos[k] = (v[0] - 0.1 * v[0], v[1] - 0.1 * v[1])
    plt.subplots()[0].set_tight_layout(False)   # remove tight layout warning by adjusting figure (index 0)
    nx.draw(display_graph, pos)
    nx.draw_networkx_labels(display_graph, custom_pos, font_color='red')
    plt.show()
