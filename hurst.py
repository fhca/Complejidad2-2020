import numpy as np


def hurst(x):
    """ Para simplificar, asumamos x es del tipo
        np.array([float,float,...]) ... """
    n = x.size
    m = x.mean()  # 1
    y = x - m  # 2
    z = y.cumsum()  # 3
    nventanas = np.log2(n)
    ventanas = np.arange(1, nventanas+1)
    e = np.zeros_like(ventanas)
    i = 0
    for ven in ventanas:
        v = int(2**ven)
        r = np.max(z[:v])-np.min(z[:v])  # 4
        s = np.std(y[:v])  # 5
        e[i] = r/s
        i += 1
    return np.polyfit(ventanas, np.log2(e), 1)[0]  # 6


# Calcula el exponente de Hurst de 100000 valores aleatorios. h[i]
# Muestra valores mínimo, máximo y std de los exponentes para 1000 experimentos
h = np.zeros(1000)
for i in range(1000):
    x = np.random.rand(100000)
    h[i] = hurst(x)
print(f"min={np.min(h)}, max={np.max(h)}, s={np.std(h)}")
