import csv


def build_graph_from_file(file_name, graph_type):
    with open(file_name) as raw_data:
        built_graph = read_graph_data(raw_data, graph_type)
        return built_graph


def read_graph_data(raw_data, graph_type):
    reader = csv.reader(raw_data, delimiter=' ')
    read_graph = None
    for line_n, line in enumerate(reader):
        if line_n == 0:
            n_vertices, = map(int, line)
            read_graph = graph_type(n_vertices)
            continue
        else:
            from_v, to_v, weight = map(int, line)
            read_graph.add_edge(from_v, to_v, weight)
    return read_graph
