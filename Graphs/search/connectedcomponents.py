from Graphs.Implementations.Graph import Graph
from Graphs.search.depthfirst import DepthFirstSearch
from Graphs.search.search import SearchStrategy, Search


class ConnectedComponents(SearchStrategy):
    def __init__(self, search):
        super().__init__(search)
        self.search = search    # type: Search
        self.graph = search.graph   # type: Graph
        self.num_vertices = self.graph.get_num_vertices()
        self.id = [0] * self.num_vertices
        self.count = 0

        def mark(waypoint):
            search.mark(waypoint)
            self.id[waypoint] = self.count

        self.search_helper = DepthFirstSearch(search, mark, immediate=False)    # type: SearchStrategy
        self.search_graph(0)

    def search_graph(self, waypoint: int) -> None:
        # strategy: go through all the vertices in the graph and perform search,
        # increase num of connected components for each unmarked vertex.
        for vertex in range(self.num_vertices):
            if not self.search.is_marked(vertex):
                self.count += 1
                self.search_helper.search_graph(vertex)

    def connected(self, vertex_a, vertex_b):
        return self.id[vertex_a] == self.id[vertex_b]

    def get_component(self, vertex):
        return self.id[vertex]
