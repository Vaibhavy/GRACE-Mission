# visualizing the original sigma square values(without correction)
import numpy as np
from matplotlib import pyplot as plt
xa=[]
i=0
for l in range(2,96):
    f=np.log(l)/np.log(10)
    xa.append(f)
log_sigma=log_sigma.reshape(94,1)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(xa,log_sigma,'g')
ax.set_aspect(aspect=0.2)
plt.show()
