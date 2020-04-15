__author__ = 'fhca'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

"""
Aquí va la descripción de cada medida que calcules. Usa "networkx"
para indicar que proviene de la biblioteca directamente. Usa el nombre
de una referencia, para indicar de que libro la sacaste. De todos modos
poner aquí la fórmula utilizada (formato LaTex, u otro).
"""

G = nx.Graph()
G.add_edges_from([("a","b"),
                  ("b","c"),
                  ("c","d"),
                  ("d","b"),
                  ])

nx.draw_networkx(G)

V = G.nodes()
n = len(V)
E = G.edges()
m = len(E)

print("n", n)
print("nodos", V)
print("m", m)
print("aristas", E)
print("excentricidad (distancia máxima a otros nodos)", nx.eccentricity(G))
print("centro (nodos con mínima excentricidad)", nx.center(G))
print("periferia (nodos con máxima excentricidad)", nx.periphery(G))
print("radio:", nx.radius(G))
print("centrality (networkx)", nx.subgraph_centrality_exp(G))
cc = nx.closeness_centrality(G)
print("cercanía (networkx)", cc)
for (k,v) in cc.items():
    cc[k]=v/(n-1)
print("cercanía (libro Barrat)", cc)
print("intermediación (networkx)", nx.betweenness_centrality(G))

plt.show()