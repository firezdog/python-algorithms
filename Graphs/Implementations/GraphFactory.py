import csv
import random
from pathlib import Path

from Graphs.Implementations.symbol_graph import SymbolGraph

DATA_DIR = Path(__file__).parent.parent / 'data'


def build_graph_from_file(file_name, graph_type):
    file_path = str(DATA_DIR / file_name)
    with open(file_path) as raw_data:
        built_graph = read_graph_data(raw_data, graph_type)
        return built_graph


def read_graph_data(raw_data, graph_type):
    if graph_type is SymbolGraph:
        return read_symbol_graph_data(raw_data, graph_type)
    data = map(int, next(raw_data).split())
    n_vertices, = data  # assumes data was not None
    new_graph = graph_type(n_vertices)
    data = next(raw_data, None)
    while data is not None:
        data = map(int, data.split())
        from_v, to_v = data
        new_graph.add_edge(from_v, to_v)
        data = next(raw_data, None)
    return new_graph


def read_symbol_graph_data(raw_data, graph_type):
    new_symbol_graph = graph_type()
    data = next(raw_data).split()
    while data is not None:
        from_v, to_v = data
        new_symbol_graph.add_edge(from_v, to_v)
        data = next(raw_data, None)
        data = data.split() if data else None
    return new_symbol_graph


def read_movie_graph_data():
    # This is different enough in format that I'll just have a specialized method.
    # TODO We can figure out how to abstract later
    file_path = str(DATA_DIR / 'movies.txt')
    with open(file_path, encoding='utf-8') as raw_data:
        new_symbol_graph = SymbolGraph()
        data = next(raw_data)
        while data is not None:
            data = iter(data.split('/'))
            movie = next(data)
            actor = next(data)
            while actor is not None:
                new_symbol_graph.add_edge(movie, actor)
                actor = next(data, None)
            data = next(raw_data, None)
    return new_symbol_graph


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
