import sys

from Graphs.graph_types import graph_types
from Graphs.GraphFactory import build_graph_from_file
from Graphs.search import Search


if __name__ == '__main__':
    file_name = sys.argv[1]
    graph_type = sys.argv[2]
    source = int(sys.argv[3])
    graph = build_graph_from_file(file_name, graph_types[graph_type])
    search = Search(graph, source)
    print('{} is connected to {}? {}'.format(source, source, search.marked(0)))
    print('Number of nodes connected to {}: {}'.format(source, search.count()))
