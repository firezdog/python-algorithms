from Graphs.search.breadthfirst import BreadthFirstSearch
from Graphs.search.connectedcomponents import ConnectedComponents
from Graphs.search.depthfirst import DepthFirstSearch
from Graphs.search.find_loop import FindLoop

search_stategies = {
    'bfs': BreadthFirstSearch,
    'dfs': DepthFirstSearch,
    'cc': ConnectedComponents,
    'loop': FindLoop
}
