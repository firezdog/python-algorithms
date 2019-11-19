import sys
from types import SimpleNamespace

from Graphs.Graph import Graph
from Graphs.adjacency_matrix import AdjacencyMatrix
from Graphs.GraphFactory import build_graph_from_file


# the number of edges at a given node
def degree(graph: Graph, vertex):
    return len(graph.get_adjacent(vertex))


def max_degree(graph: Graph):
    maximum = 0
    for vertex in range(graph.get_num_vertices()):
        next_degree = degree(graph, vertex)
        if next_degree > maximum:
            maximum = next_degree
    return maximum


# the number of nodes with edges leading back to themselves.
def self_loops(graph: Graph):
    loops = 0
    for vertex in range(graph.get_num_vertices()):
        adjacent = graph.get_adjacent(vertex)
        if vertex in adjacent:
            loops += 1
    return loops


def average_degree(graph: AdjacencyMatrix):
    sum_deg = 0
    num_vertices = graph.get_num_vertices()
    for vertex in range(num_vertices):
        sum_deg += degree(graph, vertex)
    return sum_deg / num_vertices


if __name__ == '__main__':
    file_name = sys.argv[1]
    this = SimpleNamespace()
    this.graph = build_graph_from_file('sample_graph.txt', AdjacencyMatrix)
    print('degree of V0: {}'.format(degree(this.graph, 0)))
    print('max degree: {}'.format(max_degree(this.graph)))
    print('average degree: {}'.format(average_degree(this.graph)))
    print('self loops: {}'.format(self_loops(this.graph)))
