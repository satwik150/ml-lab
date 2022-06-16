import numpy as np
from matplotlib import pyplot as plt

#inputting the vectors
a=np.array(list(map(int,input("Enter vector 1:").split())))
b=np.array(list(map(int,input("Enter vector 2:").split())))

# Adding the two vectors
c=a+b

#setting the origin
origin=[0],[0]

#Setting the X and Y axes limits
plt.xlim([-10,10])
plt.ylim([-10,10])

name1="A+B"
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#Calculating the magnitudes of a and b
mag_A=np.linalg.norm(a)
mag_B=np.linalg.norm(b)

#Calculating the magnitude of a + b
mag_AB=np.linalg.norm(c)

#Calculating the dot product of a and b
mag_ab=a@b
# @ multiplies corresponding elements of arrays and sums and returns them, so they are basically the same as dot product of a vector
# print(mag_ab)

print(f"Since |A|.|B|>=|A.B|\n{mag_A:.4f}*{mag_B:.4f}>={mag_ab:.4f}")
print("Hence it satisfies Schewartz inequality")

print(f"Since |A|+|B|>=|A+B|\n{mag_A:.4f}+{mag_B:.4f}>={mag_AB:.4f}")
print("Hence it satisfies Triangular inequality")

# scale is used to pass the vary the length of the arrows
# units is used to specify how the arrows are measured
plt.quiver(*origin,*a,scale=1,units="xy",label=f"A:{mag_A}",color="r",angles='xy')
plt.quiver(*a,*b,scale=1,units="xy",label=f"B:{mag_B}",color="g",angles='xy')
plt.quiver(*origin,*c,scale=1,units="xy",label=f"A+B:{mag_AB}",color="b",angles='xy')
plt.grid() #adds the grid in the graph
plt.legend() # adds the labelling of each arrow at the top corner of the graph
plt.show() #used to show the graph in a window