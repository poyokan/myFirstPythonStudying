import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([2,3,4,5])

fig,ax = plt.subplots()

ax.plot(x,y)
plt.show()