import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import axes3d


x=[]
y=[]
z=[]

fig1 = plt.figure()
fig2 = plt.figure()
ax1 = fig1.add_subplot(111,projection='3d')
ax2 = fig2.add_subplot(221)
ax3 = fig2.add_subplot(222)
ax4 = fig2.add_subplot(223)


with open('capture.csv' ,'r') as csvfile:

    plots = csv.reader(csvfile,delimiter = ',')

    for row in plots:

        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))


csvfile.close()

major_ticks = np.arange(-200, 200, 50)
minor_ticks = np.arange(-200, 200, 10)


ax1.set_title('3D ball')
ax1.plot3D(x,y,z)

ax2.set_title('X-Y Plane')
ax2.grid(color='g', linestyle='-', linewidth=1)
ax2.plot(x,y)
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)
ax2.set_yticks(major_ticks)
ax2.set_yticks(minor_ticks, minor=True)
ax2.grid(which='minor', alpha=0.2)
ax2.grid(which='major', alpha=0.5)


ax3.set_title('Y-Z Plane')
ax3.grid(color='g', linestyle='-', linewidth=1)
ax3.plot(y,z)
ax3.set_xticks(major_ticks)
ax3.set_xticks(minor_ticks, minor=True)
ax3.set_yticks(major_ticks)
ax3.set_yticks(minor_ticks, minor=True)
ax3.grid(which='minor', alpha=0.2)
ax3.grid(which='major', alpha=0.5)


ax4.set_title('X-Z Plane')
ax4.grid(color='g', linestyle='-', linewidth=1)
ax4.plot(x,z)
ax4.set_xticks(major_ticks)
ax4.set_xticks(minor_ticks, minor=True)
ax4.set_yticks(major_ticks)
ax4.set_yticks(minor_ticks, minor=True)
ax4.grid(which='minor', alpha=0.2)
ax4.grid(which='major', alpha=0.5)


#fig1.tight_layout()
#fig1.show()
#fig2.tight_layout()
plt.show()

