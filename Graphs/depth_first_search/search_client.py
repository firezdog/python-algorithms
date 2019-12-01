import sys

from Graphs.Implementations import Graph
from Graphs.Implementations.graph_types import graph_types
from Graphs.Implementations.GraphFactory import build_erdos_renyi_graph
from Graphs.depth_first_search.depthfirstsearch import DepthFirstSearch


def is_connected(graph: Graph, search: DepthFirstSearch) -> bool:
    return search.count() == graph.get_num_vertices()


def connection_report(graph: Graph, search: DepthFirstSearch) -> str:
    report = ''
    for node in range(graph.get_num_vertices()):
        if search.is_marked(node) and node != search.source:
            report += str(node) + ' '
    return report if report else 'No connections!'


if __name__ == '__main__':
    file_name = sys.argv[1]
    graph_type = sys.argv[2]
    source = int(sys.argv[3])
    client_graph = build_erdos_renyi_graph(graph_types[graph_type], 10, 8)
    client_search = DepthFirstSearch(client_graph, source)
    Graph.show_graph(client_graph)
    print('Connected graph? -- {}'.format(is_connected(client_graph, client_search)))
    print('Source component (excluding source) for source = {}'.format(source))
    print(connection_report(client_graph, client_search))
    for vertex in range(client_graph.get_num_vertices()):
        has_path = client_search.has_path_to(vertex)
        print('Has path to {}: {}'.format(vertex, has_path))
        if has_path:
            path = client_search.path_to(vertex)
            path.reverse()
            print(path)

