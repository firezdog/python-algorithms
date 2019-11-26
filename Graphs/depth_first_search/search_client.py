import sys

from Graphs.Implementations import Graph
from Graphs.Implementations.graph_types import graph_types
from Graphs.Implementations.GraphFactory import build_erdos_renyi_graph
from Graphs.depth_first_search.depthfirstsearch import DepthFirstSearch


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
    client_graph = build_erdos_renyi_graph(graph_types[graph_type], 5, 5)
    client_search = DepthFirstSearch(client_graph, source)
    Graph.show_graph(client_graph)
    print(is_connected(client_graph, client_search))
