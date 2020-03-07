import numpy as np
import matplotlib.pyplot as plt

def plotea(file, name):
    r0 = np.load(file+'0.npy')
    hist= np.histogramdd(r0, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
    hist_0=np.sum(hist, axis=0)#+np.sum(hist, axis=1)+np.sum(hist, axis=2)
    prod0=np.sum(hist_0*hist_0)
    sc_prod=np.empty(201)
    t=np.arange(0, 1.0001, 0.005)

    for i in range(201):
        ri=np.load(file+str(50*i)+'.npy')
        hist=np.histogramdd(ri, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
        hist_i=np.sum(hist, axis=0)#+np.sum(hist, axis=1)+np.sum(hist, axis=2)
        sc_prod[i]=np.sum(hist_i*hist_0)/prod0
    plt.plot(t,sc_prod,label='X', lw=1.0)


    hist= np.histogramdd(r0, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
    hist_0=np.sum(hist, axis=1)#+np.sum(hist, axis=1)+np.sum(hist, axis=2)
    prod0=np.sum(hist_0*hist_0)
    sc_prod=np.empty(201)
    t=np.arange(0, 1.0001, 0.005)

    for i in range(201):
        ri=np.load(file+str(50*i)+'.npy')
        hist=np.histogramdd(ri, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
        hist_i=np.sum(hist, axis=1)#+np.sum(hist, axis=1)+np.sum(hist, axis=2)
        sc_prod[i]=np.sum(hist_i*hist_0)/prod0
    plt.plot(t,sc_prod,label='Y', lw=1.0)
    hist= np.histogramdd(r0, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
    hist_0=np.sum(hist, axis=2)#+np.sum(hist, axis=1)+np.sum(hist, axis=2)
    prod0=np.sum(hist_0*hist_0)
    sc_prod=np.empty(201)
    t=np.arange(0, 1.0001, 0.005)

    for i in range(201):
        ri=np.load(file+str(50*i)+'.npy')
        hist=np.histogramdd(ri, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
        hist_i=np.sum(hist, axis=2)#+np.sum(hist, axis=1)+np.sum(hist, axis=2)
        sc_prod[i]=np.sum(hist_i*hist_0)/prod0
    plt.plot(t,sc_prod,label='Z', lw=1.0)

def plotea2(file, name):
    r0 = np.load(file+'0.npy')
    hist_0= np.histogramdd(r0, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
    prod0=np.sum(hist_0*hist_0)
    sc_prod=np.empty(201)
    t=np.arange(0, 1.0001, 0.005)

    for i in range(201):
        ri=np.load(file+str(50*i)+'.npy')
        hist_i=np.histogramdd(ri, bins=bins, range=((-L,L),(-L,L),(-L,L)))[0]
        sc_prod[i]=np.sum(hist_i*hist_0)/prod0
    plt.plot(t,sc_prod,label=name, lw=1.0)


# bins=50
#
# L=38
# plt.figure(figsize=(6,3), dpi=800)


# plotea(r'evolucio2\triangler-', 'Random')
# plotea(r'evolucio2\trianglet-', 'Hexagonal')
# plotea(r'evolucio2\triangles-', 'Square')
# plt.title('Triangle')
# plt.xlabel('Time')
# plt.ylabel(r'$\rho(t)\cdot \rho(0)$ (normalized)')
# plt.legend(ncol=3, loc=9)
# plt.xticks([0,0.25,0.5,0.75,1],['0','1/4 T','1/2 T','3/4 T','T'])
# plt.yticks((0.6,0.8,1))
# plt.ylim(0.59,1)
# plt.grid()
# plt.tight_layout()
# plt.savefig('plot_triangle.png')

# L=24
# plt.figure(figsize=(6,3), dpi=800)
# plotea(r'evolucio2\squarer-', 'Random')
# plotea(r'evolucio2\squaret-', 'Hexagonal')
# plotea(r'evolucio2\squares-', 'Square')
# plotea(r'evolucio3\squaret-', 'triangular')
# plotea(r'evolucio3\squares-', 'square')
# plotea(r'evolucio3\squaretne-', 'triang no eps')
# plt.title('Square')
# plt.xlabel('Time')
# plt.ylabel(r'$\rho(t)\cdot \rho(0)$ (normalized)')
# plt.legend(loc=9, ncol=3)
# plt.ylim(0.8,1)
# plt.xticks([0,0.25,0.5,0.75,1],['0','1/4 T','1/2 T','3/4 T','T'])
# plt.yticks((0.8,0.9,1))
# plt.grid()
# plt.tight_layout()
# plt.savefig('plot_square.png')


# plt.figure(figsize=(6,3), dpi=800)
# bins=50
# L=6.35
# plotea(r'evolucio3\circleH1-', 'H1')
# # L=4.5
# plotea(r'evolucio3\circleH4-', 'H4')
# # L=9
# plotea(r'evolucio3\circleH5-', 'H5')
# plotea(r'evolucio3\circleR-', 'R')
# L=27
# plotea(r'evolucio2\circler-', 'Random')
# plotea(r'evolucio2\circlet-', 'Hexagonal')
# plotea(r'evolucio2\circles-', 'Square')
# plt.title('Circle')
# plt.xlabel('Time')
# plt.ylabel(r'$\rho(t)\cdot \rho(0)$ (normalized)')
# plt.xticks([0, 2/7,4/7,6/7, 1],['0','2/7 T','4/7 T','6/7 T', 'T'])
# plt.yticks((0.8,0.9,1))
# plt.ylim(0.8,1)
# plt.legend(loc=8, ncol=3)
# plt.grid()
# plt.tight_layout()
# plt.savefig('plot_circle.png', dpi=300)


plt.figure(figsize=(6,3), dpi=800)

bins=30
L=9

plotea(r'evolucio3d\shpere2-', 'junk')
plotea2(r'evolucio3d\shpere2-', '3D histogram')
plt.title('Sphere')
plt.xlabel('Time')
plt.ylabel(r'$\rho(t)\cdot \rho(0)$ (normalized)')
plt.xticks([0,0.25,0.5,0.75,1],['0','1/4 T','1/2 T','3/4 T','T'])
# plt.yticks((0.8,0.9,1))
plt.ylim(0.6,1)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('plot_shpere.png', dpi=300)
