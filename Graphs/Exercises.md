4.1.1:\
the maximum number of edges for V vertices and no parallel edges -- V(V-1)/2 -- V(V-1)/2 + V = V(V+1)/2 if self loops are allowed.  Minimum number of edges to avoid isolation (=def. for some vertex V, there is no vertex W connected by an edge to V) -- I think it should be the ceiling of V/2.\
4.1.2:\
Results for adding ordered pairs in text to adjacency matrix\
0 [6, 2]\
1 [11, 8, 4]\
2 [3, 0, 6, 5]\
3 [2, 6, 10]\
4 [8, 1]\
5 [2, 10]\
6 [0, 3, 2]\
7 [11, 8]\
8 [4, 7, 11, 1]\
9 []\
10 [3, 5]\
11 [1, 7, 8]\
4.1.3:\
copying a graph: see the show graph method in Graph.py\
4.1.4:\
tell whether two vertices are adjacent: see the get_edge methods\
4.1.5:\
disallow self-loops and parallel edges: partially done by using sets -- further modification to methods would disallow adding an edge between v and w if v == w\
4.1.6:\
Impossible adj. list for 0-1, 1-2, 2-3, 3-0 no matter the order of addEdge()?\
NOTE: first  w goes into @v, then v goes into @w\
KEY IDEA: there are many possible rep's that are "correct" but that our API will never produce because of the way calls are handled.  Technically above for 11 we might have [7, 1, 8] -- but this may not be something we can produce with the API calls -- esp. if corresponding values in other arrays are in a diff. order.\
0 [3, 1] \
1 [0, 2] \
2 [1, 3] \
3 [2, 0] \
ABOVE: 0 was filled as if we first called addEdge(3,0) then addEdge(0,1) but 3 is filled as if we called (3,0) second -- impossible.\
4.1.7:\
test-client that reads and prints -- I've done one better with my own display method for matrix graphs and a visualization (using another package, admittedly)
4.18:\
UF -- skip for now
