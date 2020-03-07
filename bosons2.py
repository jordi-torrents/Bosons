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


def calmdown():
    for _ in range(10):
        nf.calmdown(r=r, v=0*v, f=F, steps=2, g=g, dt=5*dt, th=L/20, eps=0.01)
    for _ in range(10):
        nf.calmdown(r=r, v=0.33*v, f=F, steps=10, g=g, dt=5*dt, th=L/20, eps=0.01)

def initial_square():
    global r, L, v, F
    L=np.sqrt(N/rho)
    r = np.array(np.random.uniform(-L/2,L/2,(N,2)), order='F')
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    calmdown()

def initial_circle():
    global r, L, v, F
    L = np.sqrt((4/np.pi)*N/rho)
    r = np.empty((N,2), order='F')
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    n=0
    while n<N:
        pos=np.random.random(2)-0.5
        if np.sqrt(pos[0]**2+pos[1]**2)<0.5 :
            r[n]=L*pos
            n+=1
    calmdown()

def initial_circle_sq():
    global r, L, v, F, N
    dx=0.99998/np.sqrt(4*N/np.pi)
    L = np.sqrt((4/np.pi)*N/rho)
    array=np.arange(-0.5,0.5,dx)
    r = np.zeros((N,2), order='F')
    n=0
    for i in range(len(array)):
        for j in range(len(array)):
            pos=np.array([array[i], array[j]])
            if np.sqrt(pos[0]**2+pos[1]**2)<0.5 :
                r[n]=pos
                n+=1
    r=L*r[:n]
    N=len(r)
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    print(n, L, n/(0.25*np.pi*L**2))

def initial_circle_tr():
    global r, L, v, F, N
    dx=1.074465/np.sqrt(4*N/np.pi)
    dy= dx*np.sqrt(3)/2
    L = np.sqrt((4/np.pi)*N/rho)
    arrayx=np.arange(-0.5,0.5,dx)
    arrayy=np.arange(-0.5,0.5,dy)
    r = np.zeros((2*N,2), order='F')
    n=0
    for i in range(len(arrayx)):
        for j in range(len(arrayy)):
            if j%2 == 0:
                pos=np.array([arrayx[i],arrayy[j]])+(0.25*dx,0.0)
            else:
                pos=np.array([arrayx[i],arrayy[j]])-(0.25*dx,0.0)
            if np.sqrt(pos[0]**2+pos[1]**2)<0.5 :
                r[n]=pos
                n+=1
    r=L*r[:n]
    N=len(r)
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    # print(n, L, n/(0.25*np.pi*L**2))

def initial_triangle():
    global r, L, v, F
    L = np.sqrt((4/np.sqrt(3))*N/rho)
    r = np.empty((N,2), order='F')
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    h=np.sqrt(0.75)
    n=0
    while n<N:
        pos=2*np.random.random(2)-1
        if abs(pos[0])<(h*2/3-0.5*pos[1]/h) and pos[1]>1-2*h:
            r[n]=0.5*L*(pos+(0, -1+4*h/3))
            n+=1
    calmdown()

def initial_square_sq():
    global r, L, v, F, N
    n=int(np.sqrt(N))
    N=n**2
    L=np.sqrt(N/rho)
    array=np.linspace(-0.5,0.5,n)
    r = np.empty((N,2), order='F')
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    L=np.sqrt(N/rho)
    for i in range(n):
        for j in range(n):
            r[n*i+j]=(array[i], array[j])
    r=r*L

def initial_square_tr():
    global r, L, N, v, F
    n=162
    arrayx=np.linspace(-0.5,0.5,162)
    arrayy=np.linspace(-0.5,0.5,187)
    N=162*187
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    r = np.empty((N,2), order='F')
    L=np.sqrt(N/rho)
    for i in range(len(arrayx)):
        for j in range(len(arrayy)):
            r[n*j+i]=(arrayx[i], arrayy[j])
            if j%2 == 0:
                r[n*j+i] += (+0.25/(n-1), 0.0)
            else:
                r[n*j+i] += (-0.25/(n-1), 0.0)
    r=r*L

def initial_triangle_tr():
    global r, L, N, v, F
    # N=2016
    # n=63
    # N=820
    # n=40
    N=29890
    n=244
    arrayy=np.linspace(-np.sqrt(3)/6,np.sqrt(3)*4/12,n)
    arrayx=np.linspace(-0.5,0.5,n)
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
    r = np.zeros((N,2), order='F')
    L = np.sqrt((4/np.sqrt(3))*N/rho)
    k=0
    for j in range(len(arrayy)):
        for i in range(len(arrayx)-j):
            r[k]=(arrayx[i]+j*0.5/(n-1), arrayy[j])
            k+=1
    # print(k,L)
    r=r*L

def initial_triangle_sq():
    global r, L, N, v, F
    arrayx=np.linspace(-0.5,0.5,int(1.52*np.sqrt(N)))
    r = np.zeros((N,2), order='F')
    L = np.sqrt((4/np.sqrt(3))*N/rho)
    h=np.sqrt(0.75)
    k=0
    for j in arrayx:
        for i in arrayx:
            pos=np.array([i,j])*2
            if abs(pos[0])<(h*2/3-0.5*pos[1]/h) and pos[1]>1-2*h:
                r[k]=0.5*(pos+(0, -1+4*h/3))
                k+=1

    r=r[:k]
    N=len(r)
    L = np.sqrt((4/np.sqrt(3))*N/rho)
    r=L*r
    # print(k,L)
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')


N=30000
rho=10
k=(2*np.pi)**2
dt=0.0001
g=(1/3)*N/(rho**2)
t=np.zeros((1))
# initial_square()
# initial_triangle()
# initial_circle()

k=1.0
T=2*np.pi/np.sqrt(k)
dt=T/10000

# initial_square_sq()
# initial_square_tr()
# initial_triangle_tr()
initial_triangle_sq()
# initial_circle_sq()
# initial_circle_tr()


g=1.0
E_inter, E_tramp, E_kin = nf.mesure(r=r, v=v, n=N, k=k, g=g)

r = r*(E_inter/E_tramp)**(0.25)
# g=E_tramp/E_inter

E_inter, E_tramp, E_kin = nf.mesure(r=r, v=v, n=N, k=k, g=g)
print(E_inter, E_tramp, E_kin, g, k)

nf.forces(r=r, f=F, k=k, g=g)

t=np.zeros((1))
print(datetime.datetime.now())
s=0
np.save((r'evolucio8\triangleS_r-'+str(s)), r)
np.save((r'evolucio8\triangleS_v-'+str(s)), v)
for i in range(200):
    s+=50
    nf.verlet_steps(r=r, v=v, f=F, t=t, steps=50, k=k, g=g, dt=dt)
    np.save((r'evolucio8\triangleS_r-'+str(s)), r)
    np.save((r'evolucio8\triangleS_v-'+str(s)), v)
    print(t, datetime.datetime.now())
np.save((r'last_state8\triangleS_r-'+str(s)), r)
np.save((r'last_state8\triangleS_v-'+str(s)), v)
np.save((r'last_state8\triangleS_F-'+str(s)), F)


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
