#scatter plot - graphs that present the relationship between two variables in a data-set
import matplotlib.pyplot as plt
import numpy as np
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#box plot - standardized way of displaying the distribution of data based on a five number summary 
# (“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”). 
# It can tell you about your outliers and what their values are

# median is the middle number in a sorted, ascending or descending, list of numbers
#we use seed() value to reproduce the same random number on each execution
np.random.seed(10)

# random.normal(loc=0.0, scale=1.0, size=None)
# loc - Mean (“centre”) of the distribution.
# scale - Standard deviation (spread or “width”) of the distribution.
# size - Output shape, number of data points
# Variance = Square of Standard Deviation
data = np.random.normal(100, 20, 200)

# figure_name = plt.figure(figsize=(width, height))
fig = plt.figure(figsize =(10, 7))

plt.boxplot(data)

plt.show()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#heat map -  A heatmap (or heat map) is a graphical representation of data where values are depicted by color
#Proudces a array of random values of dimensions 16*16
a = np.random.random((16, 16))
# print(len(a))

# interpolation='nearest' simply displays an image without trying to interpolate(insert) between pixels 
# if the display resolution is not the same as the image resolution
# cmap - to specify the styling of the colors in graph
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#contour plot - a graphical technique for representing a 3-dimensional surface by plotting constant z slices, called contours, on a 2-dimensional format.
# linspace - Return evenly spaced numbers over a specified interval.
#evenly spaced numbers as in the difference between the two  consecutive numbers is same 
# np.linspace(2.0, 3.0, num=5) --> array([2.  , 2.25, 2.5 , 2.75, 3.  ])
feature_x = np.linspace(-5.0, 3.0, 70)
feature_y = np.linspace(-5.0, 3.0, 70)

#np.meshgrid - Return coordinate matrices from coordinate vectors.
[X, Y] = np.meshgrid(feature_x, feature_y)
fig, ax = plt.subplots(1, 1)
Z = X ** 2 + Y ** 2

ax.contourf(X, Y, Z)
ax.set_title('Filled Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')
plt.show()

#3d surface - Surface plots are diagrams of three-dimensional data. Rather than showing the individual data points, 
# surface plots show a functional relationship between a designated dependent variable (Y), and two independent variables (X and Z)
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

ax.plot_surface(x, y, z)

plt.show()
