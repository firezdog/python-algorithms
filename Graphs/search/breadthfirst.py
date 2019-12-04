from queue import Queue
from typing import List

from Graphs.Implementations.Graph import Graph
from Graphs.search.search import Search, SearchStrategy


class BreadthFirstSearch(SearchStrategy):
    def __init__(self, search: Search):
        super().__init__(search)
        self.search = search
        self.search_graph(search.source)

    def search_graph(self, waypoint: int) -> None:
        nodes_to_check = Queue()
        self.search.mark(self.search.source)
        nodes_to_check.put(self.search.source)
        while not nodes_to_check.empty():
            current = nodes_to_check.get()
            for node in self.search.get_adjacent(current):
                if not self.search.marked[node]:
                    self.search.edge_to[node] = current
                    self.search.mark(node)
                    nodes_to_check.put(node)
