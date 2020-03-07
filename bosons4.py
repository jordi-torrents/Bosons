import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numfor as nf
from time import time
import datetime
# plt.rcParams['animation.ffmpeg_path'] = r'C:\Program Files\ffmpeg\bin\ffmpeg.exe'


def animate(i):
    nf.verlet_steps(r=r, v=v, f=F, t=t, steps=1, k=k, g=g, dt=dt)
    line.set_data(r[:,0],r[:,1])
    time_text.set_text(('Time = %.4f' % t))
    return line, time_text




N=29890
# rho=10
k=(2*np.pi)**2
dt=0.0001
# g=(1/3)*N/(rho**2)
t=np.zeros((1))
v = np.zeros((N,2), order='F')
F = np.zeros((N,2), order='F')
# atracc=(1/3)*N/(rho**2)
# atracc=(1/2)*N/(rho**2) # triangle

# k=1.0
# T=2*np.pi/np.sqrt(k)
# dt=T/10000

# initial_square()
# initial_triangle()
r = np.load(r'evolucio4\triangleT_r-0.npy')
# initial_circle()

# initial_square_sq()
# initial_square_tr()
# initial_triangle_tr()
# initial_triangle_sq()
# initial_circle_sq()
# initial_circle_tr()


g=1.0
E_inter, E_tramp, E_kin = nf.mesure(r=r, v=v, k=k, g=g)

# r = r*(E_inter/E_tramp)**(0.25)
g=E_tramp/E_inter

E_inter, E_tramp, E_kin = nf.mesure(r=r, v=v, k=k, g=g)
print(E_inter, E_tramp, E_kin, g, k)

nf.forces(r=r, f=F, k=k, g=g)

t=np.zeros((1))
print(datetime.datetime.now())
s=0
np.save((r'evolucio4\triangleT_r-'+str(s)), r)
np.save((r'evolucio4\triangleT_v-'+str(s)), v)
for i in range(200):
    s+=50
    nf.verlet_steps(r=r, v=v, f=F, t=t, steps=50, k=k, g=g, dt=dt)
    np.save((r'evolucio4\triangleT_r-'+str(s)), r)
    np.save((r'evolucio4\triangleT_v-'+str(s)), v)
    print(t, datetime.datetime.now())
np.save((r'last_state4\triangleT_r-'+str(s)), r)
np.save((r'last_state4\triangleT_v-'+str(s)), v)
np.save((r'last_state4\triangleT_F-'+str(s)), F)


# fig = plt.figure()
# ax = plt.axes(xlim=(-0.6*L, 0.6*L), ylim=(-0.6*L, 0.6*L), aspect=1)
# ax.plot(0,0,'r.')
# # ax.set_xticks(())
# # ax.set_yticks(())
# line, = ax.plot(r[:,0],r[:,1], 'k.', ms=1)
# time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
# # ani = animation.FuncAnimation(fig, animate, frames=248, interval=1, blit=True, repeat=True)
# plt.show()

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Jordi Torrents'))
# ani.save('quadratic4.mp4', writer=writer)
