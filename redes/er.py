__author__ = 'fhca'

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

G = nx.Graph()

n = 300

p = .005

G.add_nodes_from(range(n))

for i in range(n):  # 0,1,2,..., n-1
    for j in range(i+1, n):  # i+1, i+2, ... , n-1
        r = np.random.random()
        if r < p:
            G.add_edge(i, j)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, alpha=.5, label=False, node_size=30)
nx.draw_networkx_edges(G, pos, label=False)
plt.show()