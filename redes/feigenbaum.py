__author__ = 'fhca'

import networkx as nx
import matplotlib.pyplot as plt

n=1000
g = nx.MultiGraph()
g.add_nodes_from(range(n))
h = nx.Graph()
for i in range(10):
    nx.add_path(h,range(0, n, 2**i))
    g.add_edges_from(h.edges())

pos = nx.spectral_layout(g)
#pos = nx.spring_layout(g, iterations=10)
#nx.draw_networkx_nodes(g, pos, node_size=1)
nx.draw_networkx_edges(g, pos)

plt.show()
