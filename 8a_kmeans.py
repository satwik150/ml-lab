import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


df = load_iris()
data = pd.DataFrame(data=df.data, columns=df.feature_names)

#scatter plot
plt.scatter(data['sepal length (cm)'],data['sepal width (cm)'])

plt.title("Before Clustering")
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

#select all rows but only columns 1 and 2
# iloc is used to select rows and columns
x = data.iloc[:,1:3] # 1st for rows and second for columns

#3 indicates the number of clusters
kmeans = KMeans(3)

# To train our model , we use kmeans.fit()
kmeans.fit(x)

# fit_predict(x) - Compute cluster centers(centroids) and predict cluster index for each sample.
# fit_predict(x) is equivalent to fit(x).predict(x).
identified_clusters = kmeans.fit_predict(x)

#gathering the data in clusters
data_in_clusters = data.copy()

# we are adding a new column called Clusters in data_in_clusters and filling those columns with the predicted clusters (stored in identified_clusters)
data_in_clusters['Clusters'] = identified_clusters
# print(data_in_clusters['Clusters']) 

ax = plt.subplot()

# c - array-like or list of colors or color, optional
sc = ax.scatter(data_in_clusters['sepal length (cm)'],data_in_clusters['sepal width (cm)'],c=data_in_clusters['Clusters'],cmap='rainbow')
plt.title("After Clustering")
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')