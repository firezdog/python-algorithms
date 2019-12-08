from typing import Callable

from Graphs.search.search import Search, SearchStrategy


class DepthFirstSearch(SearchStrategy):
    def __init__(self, search: Search, mark: Callable = None, optional_check: Callable = None, immediate=True):
        super().__init__(search)
        self.search = search    # type: Search
        self.mark = mark if mark else self.default_mark  # seems like mark has to point to parent search
        # is this ^ loose coupling?  Because a SearchStrategy has to know about a Search, but not vice versa?
        self.optional_check = optional_check if optional_check else self.default_optional_check
        if immediate:
            self.search_graph(search.source)

    def search_graph(self, current_node: int) -> None:
        """ Recursively visit and mark all nodes that can be reached from the source. """
        self.mark(current_node)
        for next_node in self.search.get_adjacent(current_node):
            if not self.search.is_marked(next_node):
                self.process_node(current_node, next_node)
                self.search_graph(next_node)
            else:
                self.optional_check()

    def default_mark(self, waypoint):
        """ This 'component' method allows me to replace marked for the connected component implementation. """
        self.search.mark(waypoint)

    def default_optional_check(self):
        pass

    def process_node(self, current_node, next_node):
        self.search.edge_to[next_node] = current_node
