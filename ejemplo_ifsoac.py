import numpy as np
import matplotlib.pyplot as plt
from time import time

t = time()
N = 10000
m = 500

# construcción de A (polígono regular de m vértices)
angulos = np.arange(0, 2*np.pi, 2*np.pi/m) + np.pi/2
A = np.array([np.cos(angulos), np.sin(angulos)]).T

# R = A[[1, 2, 0, 1, 0, 1, 2, 1, 0, 2, ...]]

# j = np.random.randint(0, m, N) # azar = donita
# descomprimir antes PCM.zip
yi = np.loadtxt("ruidos/PCM90SUE_O1.txt")
print(f"N={yi.size}")
ymin = yi.min()
ymax = yi.max()

j = ((yi-ymin)/(ymax-ymin) * m).astype(int) - 1

R = A[j]


def promedio(a, b):
    return (a + b) / 2


evalua = np.frompyfunc(promedio, 2, 1)

# Q= [A[1], (Q[-1]+A[2])/2, (Q[-1]+A[0])/2, (Q[-1]+A[1])/2, (Q[-1]+A[0])/2,...]
Q = evalua.accumulate(R, dtype=np.ndarray)

plt.figure(figsize=(5, 5))

plt.scatter(*Q.T, color='blue', s=.1, lw=0)
# plt.plot(*Q.T, ',', color='blue')

print(time()-t)
plt.show()

# time N=1e7: 28"
