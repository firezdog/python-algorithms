import csv
import random

from Graphs.graph_types import graph_types
from Graphs.Graph import show_graph


def build_graph_from_file(file_name, graph_type):
    with open(file_name) as raw_data:
        built_graph = read_graph_data(raw_data, graph_type)
        return built_graph


def read_graph_data(raw_data, graph_type):
    data = map(int, next(raw_data).split())
    n_vertices, = data
    new_graph = graph_type(n_vertices)
    data = next(raw_data, None)
    while data is not None:
        from_v, to_v = map(int, data.split())
        new_graph.add_edge(from_v, to_v)
        data = next(raw_data, None)
    return new_graph


def build_erdos_renyi_graph(graph_type, vertices, edges):
    with open('erdos_renyi.txt', 'w') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow([vertices])
        graph = graph_type(vertices)
        for edge in range(edges):
            from_vertex, to_vertex = random.randint(0, vertices - 1), random.randint(0, vertices - 1)
            writer.writerow([from_vertex, to_vertex])
            graph.add_edge(from_vertex, to_vertex)
        return graph


if __name__ == '__main__':
    chosen_graph_type = graph_types['AdjacencyMatrix']
    graph = build_erdos_renyi_graph(chosen_graph_type, 10, 4)
    show_graph(graph)
