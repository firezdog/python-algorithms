from Graphs import Graph


class Search:
    """ Given a source, determine whether an individual vertex is connected to it / how many are connected.
     Here 'connected' does not necessarily mean directly connected! """
    def __init__(self, graph: Graph, source: int):
        self.graph = graph
        self.marked = [False] * graph.get_num_vertices()
        self.depth_first_search(source)

    def depth_first_search(self, waypoint):
        """ Recursively visit and mark all nodes that can be reached from the source. """
        self.marked[waypoint] = True
        adjacent = self.graph.get_adjacent(waypoint)
        for node in adjacent:
            if not self.marked[node]:
                self.depth_first_search(node)

    def is_marked(self, vertex: int) -> bool:
        """ Is a given vertex connected to the source? """
        return self.marked[vertex]

    def count(self) -> int:
        """ How many vertices are connected to the source. """
        return sum(self.marked)
