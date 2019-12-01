import sys
from typing import Tuple

from Graphs.Implementations.Graph import Graph, show_graph
from Graphs.Implementations.graph_types import graph_types
from Graphs.Implementations.GraphFactory import build_erdos_renyi_graph
from Graphs.search.depthfirst import DepthFirstSearch


def is_connected(graph: Graph, search: DepthFirstSearch) -> bool:
    return search.count() == graph.get_num_vertices()


def connection_report(graph: Graph, search: DepthFirstSearch) -> str:
    report = ''
    for node in range(graph.get_num_vertices()):
        if search.is_marked(node) and node != search.source:
            report += str(node) + ' '
    return report if report else 'No connections!'


def build_search(graph_type: str, source: int, vertices: int, edges: int) -> Tuple[Graph, DepthFirstSearch]:
    graph = build_erdos_renyi_graph(graph_types[graph_type], vertices, edges)
    search = DepthFirstSearch(graph, source)
    return graph, search


def show_paths(graph: Graph, search: DepthFirstSearch):
    print('Connected graph? -- {}'.format(is_connected(client_graph, client_search)))
    print('Source component (excluding source) for source = {}'.format(in_source))
    print(connection_report(client_graph, client_search))
    for vertex in range(client_graph.get_num_vertices()):
        has_path = client_search.has_path_to(vertex)
        print('Has path to {}: {}'.format(vertex, has_path))
        if has_path:
            path = client_search.path_to(vertex)
            path.reverse()
            print(path)


if __name__ == '__main__':
    in_graph_type = sys.argv[1]
    in_source, in_vertices, in_edges = map(int, sys.argv[2:])
    client_graph, client_search = build_search(in_graph_type, in_source, in_vertices, in_edges)
    show_graph(client_graph)
    show_paths(client_graph, client_search)

