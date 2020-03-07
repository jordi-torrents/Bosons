import numpy as np
import matplotlib.pyplot as plt


plt.figure()
t=np.arange(0,1.0001, 0.0050)
delta_r=np.empty_like(t)


r0=np.load(r'evolucio3\triangleR-0.npy')
for i in range(len(t)):
    delta_r[i]=-np.sum((np.load(r'evolucio3\triangleR-'+str(50*i)+'.npy')-r0)**2)/30000
plt.plot(t, delta_r, label='triangleR')

r0=np.load(r'evolucio3\triangleT-0.npy')
for i in range(len(t)):
    delta_r[i]=-np.sum((np.load(r'evolucio3\triangleT-'+str(50*i)+'.npy')-r0)**2)/30000
plt.plot(t, delta_r, label='triangleT')

plt.vlines(0.25,-4,0, linestyles=':')
plt.vlines(0.5,-4,0, linestyles=':')
plt.vlines(0.75,-4,0, linestyles=':')
plt.vlines(1,-4,0, linestyles=':')
plt.legend()
plt.savefig('difussio.png')
