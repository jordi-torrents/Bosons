import numpy as np
import numfor as nf
import matplotlib.pyplot as plt

t=np.arange(0, 1.0001, 0.01)
file=r'evolucio6\triangleR_'
r0=np.load(file+'r-0.npy')
v0=np.load(file+'v-0.npy')
k=(2*np.pi)**2

# E_inter, E_tramp, E_kin = nf.mesure(r=r0, v=v0, k=k, g=1.0)
# g=E_tramp/E_inter

# g=(1/3)*len(r0)/(10**2)

g=1.0
E_inter, E_tramp, E_kin = nf.mesure(r=r0, v=v0, k=k, g=1.0)
r0*=(E_inter/E_tramp)**(0.25)
v0*=(E_inter/E_tramp)**(0.25)

E_hos=np.empty_like(t)
E_int=np.empty_like(t)
E_kin=np.empty_like(t)


for i in range(len(t)):
    print(i)
    ri=np.load(file+'r-'+str(100*i)+'.npy')*(E_inter/E_tramp)**(0.25)
    vi=np.load(file+'v-'+str(100*i)+'.npy')*(E_inter/E_tramp)**(0.25)
    E_int[i], E_hos[i], E_kin[i] = nf.mesure(r=ri, v=vi, k=k, g=g)

E_virial = -2*E_int+2*E_hos-2*E_kin
E_total  = E_int+E_hos+E_kin

plt.figure()
plt.plot(t, E_kin, label='Kinetic')
plt.plot(t, E_int, label='Interaction')
plt.plot(t, E_hos, label='H. Oscillator')
plt.plot(t, E_virial, label='Virial')
plt.plot(t, E_total, label='Total')
plt.legend()
plt.title('Triangle')
plt.xticks((0,0.25,0.5,0.75,1.0))
plt.ylabel('Energy per particle')
plt.xlabel('t / T')
plt.tight_layout()
plt.savefig('energies.png', dpi=300)
