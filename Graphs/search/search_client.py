import sys
from typing import Tuple

from Graphs.Implementations.Graph import Graph, show_graph
from Graphs.Implementations.graph_types import graph_types
from Graphs.Implementations.GraphFactory import build_erdos_renyi_graph, build_graph_from_file
from Graphs.search.search_strategies import search_stategies
from Graphs.search.search import Search


def is_connected(graph: Graph, search: Search) -> bool:
    return search.count() == graph.get_num_vertices()


def connection_report(graph: Graph, search: Search) -> str:
    report = ''
    for node in range(graph.get_num_vertices()):
        if search.is_marked(node) and node != search.source:
            report += str(node) + ' '
    return report if report else 'No connections!'


def build_search(graph_type: str, search_strategy: str, source: int, vertices: int, edges: int) -> Tuple[Graph, Search]:
    graph = build_erdos_renyi_graph(graph_types[graph_type], vertices, edges)
    # graph = build_graph_from_file('sample_graph.txt', graph_types[graph_type])
    search = Search(graph, source, search_stategies[search_strategy])
    return graph, search


def show_paths(graph: Graph, search: Search):
    print('Connected graph? -- {}'.format(is_connected(graph, search)))
    print('Source component (excluding source) for source = {}'.format(in_source))
    print(connection_report(graph, search))
    for vertex in range(graph.get_num_vertices()):
        has_path = search.has_path_to(vertex)
        print('Has path to {}: {}'.format(vertex, has_path))
        if has_path:
            path = search.path_to(vertex)
            path.reverse()
            print(path)


if __name__ == '__main__':
    in_graph_type, in_search_strategy = sys.argv[1:3]
    in_source, in_vertices, in_edges = map(int, sys.argv[3:])
    client_graph, client_search = build_search(in_graph_type, in_search_strategy, in_source, in_vertices, in_edges)
    show_graph(client_graph)
    show_paths(client_graph, client_search)
