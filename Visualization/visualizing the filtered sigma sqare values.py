# visualizing the filtered sigma sqare values
import numpy as np
from matplotlib import pyplot as plt
xa=[]
i=0
for l in range(2,96):
    f=np.log(l)/np.log(10)
    xa.append(f)
fig=plt.figure()
ax=fig.add_subplot(111)
F_log_sigma=F_log_sigma.reshape(94,1)
ax.plot(xa,F_log_sigma ,'ro')
ax.set_aspect(aspect=0.2)
plt.show()
