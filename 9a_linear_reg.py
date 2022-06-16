from sklearn import datasets,linear_model
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

k=sns.load_dataset('iris')
X=k.iloc[:30,:1].values
Y=k.iloc[:30,1:2].values
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=1/3)
model = linear_model.LinearRegression()


model.fit(x_test,y_test)
prediction = model.predict(x_test)


#Training set
plt.scatter(x_train,y_train)
plt.plot(x_test,prediction)

#Testing set
plt.scatter(x_test,y_test)
plt.plot(x_test,model.predict(x_test))