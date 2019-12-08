from queue import Queue
from typing import List, Callable

from Graphs.Implementations.Graph import Graph
from Graphs.search.search import Search, SearchStrategy


class BreadthFirstSearch(SearchStrategy):
    def __init__(self, search: Search, mark: Callable = None, optional_check: Callable = None, immediate=True):
        super().__init__(search)
        self.search = search
        self.source = self.search.source
        self.mark = mark if mark else self.default_mark
        self.optional_check = optional_check if optional_check else self.default_optional_check
        self.nodes_to_check = Queue()
        if immediate:
            self.search_graph(search.source)

    def search_graph(self, current_node: int, prev_node: int = None) -> None:
        self.search.mark(self.source)
        self.nodes_to_check.put(self.source)
        while not self.nodes_to_check.empty():
            current_node = self.nodes_to_check.get()
            for next_node in self.search.get_adjacent(current_node):
                if not self.search.is_marked(next_node):
                    self.process_node(current_node, next_node)

    def default_mark(self, node):
        self.search.mark(node)

    def default_optional_check(self):
        pass

    def process_node(self, current_node, next_node):
        self.search.edge_to[next_node] = current_node
        self.mark(next_node)
        self.nodes_to_check.put(next_node)
