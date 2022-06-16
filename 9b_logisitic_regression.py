import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data[:, :2] # we only take the first two features.
Y = iris.target

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.8,random_state=1)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)
# plt.plot(x,sig)
plt.show()


'''
import math

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
'''