from Graphs.search.search import Search, SearchStrategy


class DepthFirstSearch(SearchStrategy):
    def __init__(self, search: Search, mark=None, immediate=True):
        super().__init__(search)
        self.search = search
        if mark:
            self.mark = mark
        if immediate:
            self.search_graph(search.source)

    def search_graph(self, waypoint: int) -> None:
        """ Recursively visit and mark all nodes that can be reached from the source. """
        self.mark(waypoint)
        adjacent = self.search.get_adjacent(waypoint)
        for node in adjacent:
            if not self.search.is_marked(node):
                self.search.edge_to[node] = waypoint
                self.search_graph(node)

    def mark(self, waypoint):
        """ This 'component' method allows me to replace marked for the connected component implementation. """
        self.search.mark(waypoint)
