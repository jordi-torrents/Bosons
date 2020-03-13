import numpy as np
import numfor as nf
from time import time
import datetime

r = np.array(np.load(r'initial_states/Triangle_Hexag_30k.npy'), order='F')

N=len(r)
k=(2*np.pi)**2
dt=0.0001
t=np.zeros((1))
v = np.zeros((N,2), order='F')
F = np.zeros((N,2), order='F')

th=0.15*np.max(r)


E_inter, E_tramp, E_kin = nf.mesure_th(r=r, v=v, k=k, g=1.0, th=th)
# r = r*(E_inter/E_tramp)**(0.25)
g=E_tramp/E_inter
E_inter, E_tramp, E_kin = nf.mesure_th(r=r, v=v, k=k, g=g, th=th)
print(E_inter, E_tramp, E_kin, g, k)

nf.forces_th(r=r, f=F, k=k, g=g, th=th)

t=np.zeros((1))
print(datetime.datetime.now())
s=0
np.save((r'evolucio10/triangleT_015max_r-'+str(s)), r)
np.save((r'evolucio10/triangleT_015max_v-'+str(s)), v)
for i in range(200):
    s+=50
    nf.verlet_steps_th(r=r, v=v, f=F, t=t, steps=50, k=k, g=g, dt=dt, th=th)
    np.save((r'evolucio10/triangleT_015max_r-'+str(s)), r)
    np.save((r'evolucio10/triangleT_015max_v-'+str(s)), v)
    print(t, datetime.datetime.now())
