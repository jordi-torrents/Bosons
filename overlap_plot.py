import numpy as np
import matplotlib.pyplot as plt


t=np.arange(0, 1.0001, 0.005)
def overlap_fun(file):
    r0= np.load(file+'0.npy')
    overlap =np.empty_like(t)*0

    for i in range(len(t)):
        ri=np.load(file+str(50*i)+'.npy')
        overlap[i]= np.sum(r0*ri)/ np.sqrt(np.sum(r0**2)*np.sum(ri**2))
    return overlap


# t=np.arange(0, 1.0001, 0.005)
# r0= np.load(file+'0.npy')
# overlap =np.empty_like(t)
#
# for i in range(len(t)):
#     overlap[i]= overlap_fun(r0,np.load(file+str(50*i)+'.npy'))

plt.figure(figsize=(8,4))
plt.ylim(0.89,1.02)
plt.xlim(0,1)
# plt.plot(t, overlap_fun(r'evolucio8/triangleT_r-'), label='R dt=.0001')
# plt.plot(t, overlap_fun(r'evolucio8/triangleT_r-'), label='config 8')
# plt.plot(t, overlap_fun(r'evolucio4/triangleT_r-'), label='config 7')
plt.plot(t, overlap_fun(r'evolucio9/triangleR_r-'), label='Random')
plt.plot(t, overlap_fun(r'evolucio9/triangleS_r-'), label='Square')
plt.plot(t, overlap_fun(r'evolucio9/triangleT_r-'), label='Hexagonal')
plt.legend(ncol=3)
plt.xticks((0,0.25,0.5,0.75,1.0))
plt.yticks((0.9,0.95,1.0))
plt.grid()
plt.xlabel('Time/T')
plt.ylabel('Overlap')
plt.title('Perfectly centered')
plt.tight_layout()
plt.savefig('overlap9.png')
