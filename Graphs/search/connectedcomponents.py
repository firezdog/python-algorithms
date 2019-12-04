from Graphs.search.depthfirst import DepthFirstSearch
from Graphs.search.search import SearchStrategy


class ConnectedComponents(SearchStrategy):
    def __init__(self, search):
        super().__init__(search)
        self.search = search
        self.id = [0 * search.graph.get_num_vertices()]

        def mark(waypoint):
            search.mark(waypoint)
            self.id[waypoint] += 1

        self.search_helper = DepthFirstSearch(search, mark, immediate=False)

    def search_graph(self, waypoint: int) -> None:
        # TODO -- this will combine the logic in the init from book with the dfs helper implementation
        pass
