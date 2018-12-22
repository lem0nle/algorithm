from collections import namedtuple
from graphviz import Digraph
from .linked import LinkedList


class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [LinkedList() for _ in range(size)]

    def add_edge(self, s, t, w=1):
        Edge = namedtuple('Edge', ['target', 'weight'])
        self.edges[s].insert(Edge(t, w))

    def _repr_svg_(self):
        """Display the structure of graph in Jupyter."""
        dot = Digraph(engine='fdp')
        for i in range(self.size):
            dot.node(str(i))

        for i in range(self.size):
            for e in self.edges[i]:
                dot.edge(str(i), str(e.target), label=str(e.weight))

        return dot._repr_svg_()


class DenseGraph:
    def __init__(self, size):
        self.size = size
        self.edges = [[0] * size for _ in range(size)]

    def add_edge(self, s, t, w=1):
        self.edges[s][t] = w

    def _repr_svg_(self):
        """Display the structure of graph in Jupyter."""
        dot = Digraph(engine='fdp')
        for i in range(self.size):
            dot.node(str(i))

        for i in range(self.size):
            for j in range(self.size):
                if self.edges[i][j] == 0:
                    continue
                dot.edge(str(i), str(j), str(self.edges[i][j]))

        return dot._repr_svg_()


class FloydAllPairsSP:
    """O(v^3)"""

    def __init__(self, graph: DenseGraph):
        self.graph = graph
        self._dists = FloydAllPairsSP._floyd(graph)

    @staticmethod
    def _floyd(graph):
        size = graph.size
        d = [line[:] for line in graph.edges]
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                if d[i][j] == 0:
                    d[i][j] = float('inf')

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        return d

    def dist(self, s, t):
        return self._dists[s][t]


class DijkstraAllPairsSP:
    def __init__(self, graph: DenseGraph):
        self.graph = graph
        self._dists = DijkstraAllPairsSP._dijkstra(graph)

    @staticmethod
    def _dijkstra(graph):
        # size = graph.size
        # s = {0}
        pass
