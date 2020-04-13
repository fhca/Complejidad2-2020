__author__ = 'fhca'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

g = nx.Graph()
g.add_edge("a", "c")
g.add_edge("b", "c")
g.add_edge("c", "e")
g.add_edges_from([("e","d"),
                  ("e","g"),
                  ("e","f")])
g.add_edges_from([("f","g"),
                  ("f","j")
                  ])
g.add_edges_from([("i","h"),
                  ("i","g"),
                  ("i","j")])
g.add_edge("h","g")
g.add_edge("j","g")
nx.draw_networkx(g)
nodos_ordenados = np.sort(g.nodes())
print(nx.to_numpy_matrix(g, nodelist=nodos_ordenados))
print("excentricidad (distancia máxima a otros nodos)", nx.eccentricity(g))
print("centro (nodos con mínima excentricidad)", nx.center(g))
print("periferia (nodos con máxima excentricidad)", nx.periphery(g))
print("radio:", nx.radius(g))
plt.show()
