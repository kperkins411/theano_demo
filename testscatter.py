__author__ = 'Keith'
import matplotlib.pyplot as plt
import numpy as np

abc = range(20)
xyc = [16*np.random.randint(0,2)+2 for i in range(20)]

plt.subplot(121)
plt.scatter(abc[:13], abc[:13], c=xyc[:13], s=35, vmin=0, vmax=20)
plt.colorbar()
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.subplot(122)
plt.scatter(abc[8:20], abc[8:20], c=xyc[8:20], s=35, vmin=0, vmax=20)
plt.colorbar()
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()