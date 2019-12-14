from typing import Callable

from Graphs.search.depthfirst import DepthFirstSearch
from Graphs.search.search import SearchStrategy


class FindLoop(SearchStrategy):
    def __init__(self, search):
        super().__init__(search)
        self.has_loop = False

        def check_has_loop(prev_node, current_node, next_node):
            if prev_node != next_node:
                self.has_loop = True

        self.search_helper = DepthFirstSearch(search, optional_check=check_has_loop)

    def search_graph(self, current_node: int, next_node: int) -> None:
        pass
