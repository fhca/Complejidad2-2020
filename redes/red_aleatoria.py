__author__ = 'fhca'

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
G = nx.random_geometric_graph(200, 0.125)
# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, 'pos')

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center
p = nx.single_source_shortest_path_length(G, ncenter)

plt.figure(figsize=(8, 8))
nx.draw_networkx_edges(G, pos,alpha=0.4)
nx.draw_networkx_nodes(G, pos, nodelist=[ncenter], alpha=0.4, node_color='green')
nx.draw_networkx_nodes(G, pos, nodelist=p.keys(), node_size=80)

plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.axis('off')
plt.show()