from Graphs.search.search import Search, SearchStrategy


class DepthFirstSearch(SearchStrategy):
    def __init__(self, search: Search):
        super().__init__(search)
        self.search = search
        self.search_graph(search.source)

    def search_graph(self, waypoint: int) -> None:
        """ Recursively visit and mark all nodes that can be reached from the source. """
        self.search.mark(waypoint)
        adjacent = self.search.get_adjacent(waypoint)
        for node in adjacent:
            if not self.search.marked[node]:
                self.search.edge_to[node] = waypoint
                self.search_graph(node)
