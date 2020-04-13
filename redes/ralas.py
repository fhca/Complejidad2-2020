__author__ = 'fhca'

import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')  # para que pycharm saque la grafica en ventana nueva

def linea(n):
    "L_{n}, también llamada cadena"
    G = nx.Graph()
    #G.add_nodes_from(range(n))
    #G.add_edges_from([(0,1), (1,2), (2,3), (3,4), (4,5)])
    for i in range(n-1):
        G.add_edge(i, i+1)
    return G

def ciclo(n):
    "C_n "
    G = nx.Graph()
    for i in range(n-1):
        G.add_edge(i, i+1)
    G.add_edge(n-1, 0)
    return G

def completa(n):
    G = nx.Graph()
    for i in range(n):
        for j in range(i):
            G.add_edge(i, j)
    return G

G = ciclo(5)
nx.draw(G, with_labels=True)
print(list(G.adjacency()))
plt.show()