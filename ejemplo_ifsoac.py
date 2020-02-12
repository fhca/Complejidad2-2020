import numpy as np
import matplotlib.pyplot as plt
from time import time

t = time()
N = 5000000

A = np.array(((0, 0), (1, 0), (.5, np.sqrt(3)/2)))

# R = A[[1, 2, 0, 1, 0, 1, 2, 1, 0, 2, ...]]
j = np.random.randint(0, 3, N)
R = A[j]


def promedio(a, b):
    return (a + b) / 2


evalua = np.frompyfunc(promedio, 2, 1)

# Q= [A[1], (Q[-1]+A[2])/2, (Q[-1]+A[0])/2, (Q[-1]+A[1])/2, (Q[-1]+A[0])/2,...]
Q = evalua.accumulate(R, dtype=np.ndarray)

plt.scatter(*Q.T, color='blue', s=.1, lw=0)
# plt.plot(*Q.T, ',', color='blue')

print(time()-t)
plt.show()

# time N=1e7: 28"
