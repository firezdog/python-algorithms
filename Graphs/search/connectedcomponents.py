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

        def mark(current_node):
            search.mark(current_node)
            self.id[current_node] = self.count

        self.search_helper = DepthFirstSearch\
            (search, mark=mark, optional_check=None, immediate=False)   # type: SearchStrategy
        self.search_graph()

    def search_graph(self, current_node: int = 0, prev_node: int = 0) -> None:
        # strategy: go through all the vertices in the graph and perform search,
        # increase num of connected components for each unmarked vertex.
        # N.B. current_node is irrelevant since we go through all
        for vertex in range(self.num_vertices):
            if not self.search.is_marked(vertex):
                self.count += 1
                self.search_helper.search_graph(vertex)

    def connected(self, vertex_a, vertex_b):
        return self.id[vertex_a] == self.id[vertex_b]

    def get_component(self, vertex):
        return self.id[vertex]
