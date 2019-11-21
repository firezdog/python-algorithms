from Graphs import Graph


class Search:
    """ Given a source, determine whether an individual vertex is connected to it / how many are connected. """
    def __init__(self, graph: Graph, source: int):
        self.graph = graph
        self.source = source

    def marked(self, vertex: int) -> bool:
        """ Is a given vertex connected to the source? """
        # initial pass -- check if vertex is in adj(source)
        adjacent = self.graph.get_adjacent(vertex)
        return self.source in adjacent

    def count(self) -> int:
        """ How many vertices are connected to the source? (counting self-loops and parallel edges?) """
        adj_to_source = self.graph.get_adjacent(self.source)
        # source only needs to be connected to every OTHER vertex (self loops are allowed but not required)
        return len(adj_to_source) + 1
