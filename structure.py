import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numfor as nf
from time import time
import datetime
# plt.rcParams['animation.ffmpeg_path'] = r'C:\Program Files\ffmpeg\bin\ffmpeg.exe'




def calmdown():
    for _ in range(5):
        nf.verlet_steps_eps(r=r,v=np.zeros((N,2), order='F'),f=F,t=0.0,steps=20,tramp=0.0,atracc=atracc, dt=0.0001, th=th, eps=eps)
    for _ in range(3):
        nf.verlet_steps_eps(r=r,v=np.zeros((N,2), order='F'),f=F,t=0.0,steps=60,tramp=0.0,atracc=atracc, dt=0.0001, th=th, eps=eps)

def initial_square():
    global r, L, v, F
    L=np.sqrt(N/rho)
    r = np.array(np.random.uniform(-L/2,L/2,(N,2)), order='F')
    v = np.zeros((N,2), order='F')
    F = np.zeros((N,2), order='F')
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
    n=21
    arrayx=np.linspace(-0.5,0.5,n)
    arrayy=np.linspace(-0.5,0.5,23)
    N=n*23
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


N=500
rho=15
atracc=(1/3)*N/(rho**2)
th=10
eps=1.e-4
L=np.sqrt(N/rho)
# initial_square()
# initial_square_sq()
# initial_square_tr()


fig, axs = plt.subplots(1,3, figsize=(11,3), dpi=800)
for ax in axs:
    ax.set(xlim=(-0.6*L, 0.6*L), ylim=(-0.6*L, 0.6*L), aspect=1, xticks=(), yticks=())
initial_square()
print(len(r), N)
axs[0].plot(r[:,0],r[:,1], 'k.', ms=2)
initial_square_sq()
print(len(r), N)
axs[1].plot(r[:,0],r[:,1], 'k.', ms=2)
initial_square_tr()
print(len(r), N)
axs[2].plot(r[:,0],r[:,1], 'k.', ms=2)
plt.tight_layout()
plt.savefig('structure.png')
