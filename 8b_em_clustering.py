# EM Clustering

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas import DataFrame 
from sklearn import datasets 
from sklearn.mixture import GaussianMixture


iris = datasets.load_iris()  
#extracting all rows but only column 0 and 1
X = iris.data[:, :2]   
# print(X)

#converting into pandas dataframe
d = pd.DataFrame(X) 
# print(d)
plt.scatter(d[0], d[1])

# GaussianMixture object implements the expectation-maximization (EM) algorithm
# so it is same as using the EM clustering algo
gmm = GaussianMixture(n_components = 3)

#training the model
gmm.fit(d)  

#predicting the clusters and storing the labels of clusters
labels = gmm.predict(d) 
# print("labels")
# print(labels)

#creating a new column in d dataframe called as labels and storing the label values in it
d['labels']= labels 

#storing data of different clusters in different variables
d0 = d[d['labels']== 0] 
d1 = d[d['labels']== 1] 
d2 = d[d['labels']== 2] 

#plotting the clusters
#since each clusters will have two columns so we are using d0[0],d0[1]
plt.scatter(d0[0], d0[1], c ='r') 
plt.scatter(d1[0], d1[1], c ='yellow') 
plt.scatter(d2[0], d2[1], c ='g')