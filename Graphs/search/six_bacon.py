from Graphs.search.breadthfirst import BreadthFirstSearch
from Graphs.search.search import Search
from Graphs.Implementations.GraphFactory import read_movie_graph_data

if __name__ == '__main__':
    target = "Bacon, Kevin"
    print("Playing six degrees of {}.  Please input an actor.".format(target))
    actor = input()
    graph = read_movie_graph_data()
    target_code = graph.vertex_map[target]
    try:
        actor_code = graph.vertex_map[actor]
        search = Search(graph, target_code, BreadthFirstSearch)
        if search.has_path_to(actor_code):
            path = iter(search.path_to(actor_code))
            actor_a_code = next(path, None)
            movie_code = next(path, None)
            actor_b_code = next(path, None)
            while actor_b_code is not None:
                print('{} in {} with {}'.format(
                    graph.vertex_map[actor_a_code],
                    graph.vertex_map[movie_code],
                    graph.vertex_map[actor_b_code])
                )
                actor_a_code = actor_b_code
                movie_code = next(path, None)
                actor_b_code = next(path, None)
        else:
            print("No relation...")
    except:
        print("That didn't work...")
