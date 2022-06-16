import numpy as np
import matplotlib.pyplot as plt

def plt2d(v,color):
    origin=[0,0]
    plt.quiver(*origin,*v,color=color,angles='xy',scale_units='xy',scale=1)
    
def plt3d(ax,v,color):
    ax.quiver(*[0,0,0],*v,color=color)

#2d
x=[20,30]
y=[45,23]
z=[-33,-43]

plt.xlim(-50,50)
plt.ylim(-50,50)

plt2d(x,'r')
plt2d(y,'g')
plt2d(z,'b')

# ----------------------------------------------------------------------------------------------------
#3d
v1=[1, 2, 3]
v2=[-7, -4, 2]
v3=[3, 4, -2]

#To increase the size of the graph, (5,5) indicates the width and height in inches
fig=plt.figure(figsize=(5,5))

#this plots a 3d empty graph on top of fig plane
ax=plt.axes(projection='3d')

#to set the x, y and z limits
plt.xlim([-10,10])
plt.ylim([-10,10])
ax.set_zlim([-10,10])

plt3d(ax,v1,'r')
plt3d(ax,v2,'b')
plt3d(ax,v3,'g')

# ----------------------------------------------------------------------------------------------------

#vector addition
x1=np.array([20,30])
y1=np.array([45,23])

plt.xlim([-50,90])
plt.ylim([-50,90])

plt2d(x1,'r')
plt2d(y1,'g')
plt2d(x1+y1,'b')

#subtraction
plt2d(x1-y1,'y')

# ----------------------------------------------------------------------------------------------------

#cross product
j1=[1, 2, 3]
j2=[-7, -4, 2]

fig=plt.figure(figsize=(5,5))
ax=plt.axes(projection='3d')


plt.xlim([-10,10])
plt.ylim([-10,10])
ax.set_zlim([-10,10])

plt3d(ax,j1,'r')
plt3d(ax,j2,'b')
plt3d(ax,np.cross(j1,j2),'g')