# visualizing the all three types sigma sqare values
import numpy as np
from matplotlib import pyplot as plt
xa=[]
i=0
for l in range(2,96):
    f=np.log(l)/np.log(10)
    xa.append(f)
fig=plt.figure()
ax=fig.add_subplot(111)
aax=fig.add_subplot(111)
aaax=fig.add_subplot(111)
ax.set_ylabel('log( Sigma^2)')
ax.set_xlabel('log(l)')
F_log_sigma=F_log_sigma.reshape(94,1)
aaax.plot(xa,log_sigma ,'b', label='Original')
F_log_sigma=F_log_sigma.reshape(94,1)
ax.plot(xa,F_log_sigma ,'g', label='Filtered')
aax.plot(xa, corrected_sigma_square_values,'r',label='Approaximated' )
aax.legend()
ax.legend()
aaax.legend()
ax.set_aspect(aspect=.05)
fig.savefig('equal.png')
plt.show()
