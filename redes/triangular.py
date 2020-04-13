__author__ = 'fhca'

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


G = nx.triangular_lattice_graph(20,20)
plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G, iterations=200)
nx.draw_networkx_nodes(G, pos, node_size=1)
nx.draw_networkx_edges(G, pos, alpha=.5)

plt.show()

"""
from networkx.drawing.nx_pydot import write_dot
G = nx.triangular_lattice_graph(20,20)
pos = nx.nx_agraph.graphviz_layout(G)
nx.draw(G, pos=pos)
write_dot(G, 'file.gv')
"""