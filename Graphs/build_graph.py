import sys
from Graphs.adjacency_matrix import AdjacencyMatrix

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file) as raw_data:
        graph = None
        try:
            line = next(raw_data).split()
            try:
                n_vertices = int(line[0])
                graph = AdjacencyMatrix(n_vertices)
                while True:
                    line = next(raw_data).split()
                    try:
                        _from, to, weight = map(int, line)
                        graph.add_edge(_from, to, weight)
                    except ValueError as e:
                        print("Error in file format. Processing stopped.")
                        raise e
            except ValueError as e:
                print("Error in file format.  Processing stopped.")
                raise e
        except StopIteration:
            graph.render()
            print(graph.get_edges())
            print(graph.get_adjacent(3))
