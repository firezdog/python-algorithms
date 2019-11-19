from Graphs.Graph import Graph


class AdjacencyMatrix(Graph):
    def __init__(self, num_vertices):
        self.cell_size = 6
        self.matrix = [[0 for y in range(num_vertices)] for x in range(num_vertices)]
        self.edges = set()

    def set_render_cell_size(self, cell_size):
        self.cell_size = cell_size

    # will over-write existing edge
    def add_edge(self, from_vertex, to_vertex, **kwargs):
        self.matrix[from_vertex][to_vertex] = 1
        self.matrix[to_vertex][from_vertex] = 1
        edge = frozenset({from_vertex, to_vertex})
        self.edges.add(edge)

    def get_edges(self):
        return self.edges

    # note -- for an undirected graph, an edge from A to B counts as an edge from B to A, so...how many edges?
    def get_num_edges(self):
        return len(self.edges)

    def get_edge(self, vertex_a, vertex_b):
        # prob faster than iterating through edge list
        return self.matrix[vertex_a][vertex_b] != 0

    def get_num_vertices(self):
        return len(self.matrix)

    def get_adjacent(self, vertex_a):
        adjacent = list()
        for vertex, weight in enumerate(self.matrix[vertex_a]):
            if weight != 0:
                adjacent.append(vertex)
        return adjacent

    def render(self, print_out=True):
        rep = ' ' * self.cell_size
        for i, row in enumerate(self.matrix):
            col_header = 'V{}'.format(i)
            rep += '{}{}'.format(col_header, ' ' * (self.cell_size - len(col_header)))
        rep += '\n'
        for i, row in enumerate(self.matrix):
            row_header = 'V{}'.format(i)
            rep += '{}{}'.format(row_header, ' ' * (self.cell_size - len(row_header)))
            for edge in row:
                rep += str(edge) + ' ' * (self.cell_size - len(str(edge)))
            rep += '\n' if i < len(self.matrix) - 1 else ''
        if print_out:
            print(rep)
        return rep

