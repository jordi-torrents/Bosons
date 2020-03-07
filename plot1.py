import numpy as np
import matplotlib.pyplot as plt

bins=100
vmax=0.1*165000/bins**2
vmax=10.5
L=45
L=23

def plotea(file, name):
    r1=np.load(file+'_r-0.npy')
    r2=np.load(file+'_r-1250.npy')
    r3=np.load(file+'_r-2500.npy')
    r4=np.load(file+'_r-3750.npy')
    r5=np.load(file+'_r-5000.npy')
    r6=np.load(file+'_r-6250.npy')
    r7=np.load(file+'_r-7500.npy')
    r8=np.load(file+'_r-8750.npy')
    fig, axs = plt.subplots(2,4, figsize=(10,5), dpi=800)
    for ax, r, title in zip(axs.flat, (r1,r2,r3,r4,r5, r6, r7,r8), range(8)):
        ax.set(xlim=(-L,L), ylim=(-L,L), xticks=(), yticks=(), aspect=1)
        ax.hist2d(r[:,0], r[:,1], cmap='inferno', vmax=vmax, bins=bins, range=((-L,L),(-L,L)))
        ax.set(title=('$t = %i/8 T$' % title))
    plt.tight_layout()
    plt.savefig(name)

def plotea2(file, name):
    r1=np.load(file+'-0.npy')
    r2=np.load(file+'-1450.npy')
    r3=np.load(file+'-2800.npy')
    r4=np.load(file+'-4300.npy')
    r5=np.load(file+'-5650.npy')
    r6=np.load(file+'-7150.npy')
    r7=np.load(file+'-8450.npy')
    r8=np.load(file+'-10000.npy')
    fig, axs = plt.subplots(2,4, figsize=(10,5), dpi=800)
    for ax, r, title in zip(axs.flat, (r1,r2,r3,r4,r5, r6, r7,r8), range(8)):
        ax.set(xlim=(-L,L), ylim=(-L,L), xticks=(), yticks=(), aspect=1)
        ax.hist2d(r[:,0], r[:,1], cmap='inferno', vmax=vmax, bins=bins, range=((-L,L),(-L,L)))
        ax.set(title=(r'$t = %i/7 T$' % title))
    plt.tight_layout()
    plt.savefig(name)
# L=40
# bins=150
# vmax=7.5
# plotea(r'\squarer')
# plotea(r'\squares')
# plotea(r'\squaret')

# plotea(r'\triangleT')
# L=44
# bins=150
# vmax=7.5
# plotea(r'\triangler')
# plotea(r'\trianglet2')
# plotea(r'\triangles')
# L=35
# bins=150
# vmax=6.5
# # plotea2(r'\circler')
# L=6.35
# bins=30
# L=6.333
# plotea2(r'\circleH1')
# plotea2(r'\circleH4')
# plotea2(r'\circleH5')
# plotea2(r'\circles')
# bins=80
# vmax=20
bins=120
vmax=None
L=45

# plotea(r'evolucio3d\shpere', 'shpere.png')
plotea(r'evolucio5\triangleR', 'pack-triangle.png')
