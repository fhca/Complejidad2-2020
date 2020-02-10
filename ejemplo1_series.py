import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(1000000) - .5
r45 = np.arange(1000)
y = x.cumsum()
plt.plot(y)
plt.show()
