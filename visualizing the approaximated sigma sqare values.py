# visualizing the approaximated sigma sqare values
import numpy as np
from matplotlib import pyplot as plt
xa=[]
i=0
for l in range(2,96):
    f=np.log(l)/np.log(10)
    xa.append(f)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(xa,corrected_sigma_square_values ,'b')
ax.set_aspect(aspect=0.2)
plt.show()
