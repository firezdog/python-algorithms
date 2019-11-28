4.1.1:\
the maximum number of edges for V vertices and no parallel edges -- V(V-1)/2 -- V(V-1)/2 + V = V(V+1)/2 if self loops are allowed.  Minimum number of edges to avoid isolation (=def. for some vertex V, there is no vertex W connected by an edge to V) -- I think it should be the ceiling of V/2.\
4.1.3:\
copying a graph: see the show graph method in Graph.py\
4.1.4:\
tell whether two vertices are adjacent: see the get_edge methods\
4.1.5:\
disallow self-loops and parallel edges: partially done by using sets -- further modification to methods would disallow adding an edge between v and w if v == w\
4.1.7:\
test-client that reads and prints -- I've done one better with my own display method for matrix graphs and a visualization (using another package, admittedly)
