import csv
import random
from pathlib import Path

from Graphs.Implementations.graph_types import graph_types
from Graphs.Implementations.Graph import show_graph

DATA_DIR = Path(__file__).parent.parent / 'data'


def build_graph_from_file(file_name, graph_type):
    file_path = str(DATA_DIR / 'erdos_renyi.txt')
    with open(file_path) as raw_data:
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
    file_path = str(DATA_DIR / 'erdos_renyi.txt')
    with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow([vertices])
        built_graph = graph_type(vertices)
        for edge in range(edges):
            from_vertex, to_vertex = random.randint(0, vertices - 1), random.randint(0, vertices - 1)
            writer.writerow([from_vertex, to_vertex])
            built_graph.add_edge(from_vertex, to_vertex)
        return built_graph


if __name__ == '__main__':
    chosen_graph_type = graph_types['AdjacencyMatrix']
    graph = build_erdos_renyi_graph(chosen_graph_type, 15, 20)
    graph.render()
    show_graph(graph)
