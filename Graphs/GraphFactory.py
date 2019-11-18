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
        from_v, to_v, weight = map(int, data.split())
        new_graph.add_edge(from_v, to_v, weight)
        data = next(raw_data, None)
    return new_graph
