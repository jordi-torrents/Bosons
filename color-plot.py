import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    r = np.load('evolucio9/triangleS_r-'+str(50*i)+'.npy')
    red_line.set_data(r[red_index,0],r[red_index,1])
    blu_line.set_data(r[blu_index,0],r[blu_index,1])
    gre_line.set_data(r[gre_index,0],r[gre_index,1])
    yel_line.set_data(r[yel_index,0],r[yel_index,1])
    text.set_text(('Time: %.3f' % float(0.005*i)))
    return red_line, blu_line, gre_line, yel_line, text

r0 = np.load('evolucio9/triangleS_r-0.npy')

# red_index = np.where((r0[:,0]<0)*(r0[:,1]<0))
# blu_index = np.where((r0[:,0]>0)*(r0[:,1]<0))
# gre_index = np.where((r0[:,0]<0)*(r0[:,1]>0))
# yel_index = np.where((r0[:,0]>0)*(r0[:,1]>0))

red_index = np.where(np.sqrt(r0[:,0]**2+r0[:,1]**2)<9)
blu_index = np.where((np.sqrt(r0[:,0]**2+r0[:,1]**2)>9)*(np.sqrt(r0[:,0]**2+r0[:,1]**2)<18))
gre_index = np.where((np.sqrt(r0[:,0]**2+r0[:,1]**2)>18)*(np.sqrt(r0[:,0]**2+r0[:,1]**2)<30))
yel_index = np.where((np.sqrt(r0[:,0]**2+r0[:,1]**2)>30)*(np.sqrt(r0[:,0]**2+r0[:,1]**2)<400))

L=60
fig, ax = plt.subplots(1, figsize=(6,6))
ax.axis('off')
ax.set(aspect=1, xlim=(-L,L), ylim=(-L,L))
red_line = ax.plot([],[],'C0.', ms=1)[0]
blu_line = ax.plot([],[],'C1.', ms=1)[0]
gre_line = ax.plot([],[],'C2.', ms=1)[0]
yel_line = ax.plot([],[],'C3.', ms=1)[0]
text = ax.text(0.02, 0.92, '', transform=ax.transAxes)
plt.tight_layout()

ani = animation.FuncAnimation(fig, animate, frames=201, interval=40, blit=True, repeat=False)

ani.save('video_triangle_Square2.mp4', fps=20, dpi=150)
