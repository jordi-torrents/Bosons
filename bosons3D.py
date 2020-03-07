import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numfor as nf
from time import time
import datetime
# plt.rcParams['animation.ffmpeg_path'] = r'C:\Program Files\ffmpeg\bin\ffmpeg.exe'


def animate(i):
    nf.verlet_steps_eps_3d(r=r,v=v,f=F,t=t,steps=5,k=k,g=g, dt=dt, th=th, eps=eps)
    line.set_data(r[:,2],r[:,1])
    time_text.set_text(('Time = %.4f' % t))
    return line, time_text


def calmdown():
    for _ in range(15):
        nf.verlet_steps_eps_3d(r=r,v=0*v,f=F,t=0.0,steps=10,k=0.0,g=g, dt=0.0001, th=1.0, eps=eps)
    # for _ in range(3):
    #     nf.verlet_steps_eps_3d(r=r,v=0*v,f=F,t=0.0,steps=5,k=0.0,g=g, dt=0.0001, th=1.0, eps=eps)

def initial_square():
    global r, L, v, F
    L=(N/rho)**(1/3)
    r = np.array(np.random.uniform(-L/2,L/2,(N,3)), order='F')
    v = np.zeros((N,3), order='F')
    F = np.zeros((N,3), order='F')
    calmdown()

def initial_circle():
    global r, L, v, F
    L = ((6/np.pi)*N/rho)**(1/3)
    r = np.empty((N,3), order='F')
    v = np.zeros((N,3), order='F')
    F = np.zeros((N,3), order='F')
    n=0
    while n<N:
        pos=np.random.random(3)-0.5
        if np.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)<0.5 :
            r[n]=L*pos
            n+=1
    calmdown()


N=30000
rho=15
k=(2*np.pi)**2
g=(1/6)*N/(rho**3)
dt=0.001
eps=0.0
th=1000000.0

# initial_square()
initial_circle()

t=np.zeros((1))



print(datetime.datetime.now())
s=0
np.save((r'evolucio3d\shpere2-'+str(s)), r)
for i in range(200):
    s+=50
    nf.verlet_steps_eps_3d(r=r,v=v,f=F,t=t,steps=5,k=k,g=g, dt=dt, th=th, eps=eps)
    print(t)
    np.save((r'evolucio3d\shpere2-'+str(s)), r)
    print(datetime.datetime.now())
np.save((r'last_state\shpere2_r-'+str(s)), r)
np.save((r'last_state\shpere2_v-'+str(s)), v)
np.save((r'last_state\shpere2_F-'+str(s)), F)


# fig = plt.figure()
# ax = plt.axes(xlim=(-0.6*L, 0.6*L), ylim=(-0.6*L, 0.6*L), aspect=1)
# ax.plot(0,0,'r.')
# # ax.set_xticks(())
# # ax.set_yticks(())
# line, = ax.plot(r[:,2],r[:,1], 'k.', ms=1)
# time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
# # ani = animation.FuncAnimation(fig, animate, frames=248, interval=1, blit=True, repeat=True)
# plt.show()

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Jordi Torrents'))
# ani.save('quadratic4.mp4', writer=writer)
