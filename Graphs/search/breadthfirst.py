from queue import Queue
from typing import List

from Graphs.Implementations.Graph import Graph


# TODO: make parent class for search (or use strategy pattern?)
class BreadFirstSearch:
    def __init__(self, graph: Graph, source: int):
        self.edge_to = [-1 * graph.get_num_vertices()]
        self.marked = [False * graph.get_num_vertices()]
        self.source = source
        self.breadth_first_search(graph, source)

    def breadth_first_search(self, graph: Graph, source: int) -> None:
        nodes_to_check = Queue()
        self.marked[source] = True
        nodes_to_check.put(self.source)
        while not nodes_to_check.empty():
            current = nodes_to_check.get()
            for node in graph.get_adjacent(current):
                if not self.marked[node]:
                    self.edge_to[node] = current
                    self.marked[node] = True
                    nodes_to_check.put(node)

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
