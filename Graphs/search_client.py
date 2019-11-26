import sys

from Graphs.Implementations import Graph
from Graphs.Implementations.graph_types import graph_types
from Graphs.Implementations.GraphFactory import build_graph_from_file
from Graphs.depthfirstsearch import DepthFirstSearch


def is_connected(graph: Graph, search: DepthFirstSearch) -> bool:
    connection_report = ''
    for vertex in range(graph.get_num_vertices()):
        if search.is_marked(vertex):
            connection_report += str(vertex) + ' '
    print(connection_report)
    return search.count() == graph.get_num_vertices()


if __name__ == '__main__':
    file_name = sys.argv[1]
    graph_type = sys.argv[2]
    source = int(sys.argv[3])
    client_graph = build_graph_from_file(file_name, graph_types[graph_type])
    client_search = DepthFirstSearch(client_graph, source)
    print(is_connected(client_graph, client_search))
