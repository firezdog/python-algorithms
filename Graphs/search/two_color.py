from typing import Callable

from Graphs.search.depthfirst import DepthFirstSearch
from Graphs.search.search import SearchStrategy, Search


class TwoColor(SearchStrategy):
    def __init__(self, search: Search):
        super().__init__(search)
        self.search = search
        self.graph = self.search.graph
        self.num_vertices = self.graph.get_num_vertices()
        self.color = [False] * self.num_vertices
        self.is_two_colorable = True

        def process_node(current_node, next_node):
            self.color[next_node] = not self.color[current_node]

        def optional_check(prev_node, current_node, next_node):
            if current_node == next_node:
                return
            if self.color[current_node] == self.color[next_node]:
                self.is_two_colorable = False

        self.search_helper = DepthFirstSearch(search, process_node=process_node, optional_check=optional_check,
                                              immediate=False)
        self.search_graph(-1, -1)

    def search_graph(self, current_node: int, prev_node: int) -> None:
        for vertex in range(self.num_vertices):
            if not self.search.is_marked(vertex):
                self.search_helper.search_graph(vertex, vertex)

    def is_bipartite(self):
        return self.is_two_colorable

