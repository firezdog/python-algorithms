from typing import Callable

from Graphs.search.depthfirst import DepthFirstSearch
from Graphs.search.search import SearchStrategy


class FindLoop(SearchStrategy):
    def __init__(self, search, mark: Callable = None, optional_check: Callable = None, immediate=True):
        super().__init__(search)
        self.has_loop = False

        def check_has_loop(node_a: int, node_b: int):
            print("running custom check for {} and {}".format(node_a, node_b))
            if node_a != node_b:
                self.has_loop = True
                print("Found a loop!")

        self.search_helper = DepthFirstSearch(search, optional_check=check_has_loop)

    def search_graph(self, current_node: int, next_node: int) -> None:
        pass
