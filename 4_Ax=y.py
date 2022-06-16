#AX = Y
import numpy as np
import matplotlib.pyplot as plt

origin = [0], [0]
m_list = [[4, 3], [-5, 9]]
A = np.array(m_list)
B = np.array([20, 26])

#AX = B
#X = A^-1 * B
X = np.linalg.inv(A).dot(B)

print("X=",X)

#setting figure size
# plt.rcParams["figure.figsize"] = (20,20)
fig = plt.figure(figsize=(10,10))

#plotting m_list or A
plt.quiver(*origin, *m_list[0],scale=1,color='r',units='xy',label='A')
plt.quiver(*origin, *m_list[1],scale=1,color='g',units='xy',label='B')

#plotting B
plt.quiver(*origin, *B,scale=1,color='b',units='xy',label='Coeff')

#plotting X
plt.quiver(*origin, *X,scale=1,color='orange',units='xy',label='X')

# setting X and Y axes limits
plt.xlim(-10, 30)
plt.ylim(-10, 30)

#customizing the Ax=Y text
plt.text(21, 28, 'Ax=Y', fontsize = 22, bbox = dict(facecolor = 'red', alpha = 0.5))

plt.grid()
plt.legend()
plt.show()