import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

#Load data from builtin sklearn datasets
data = load_iris()

#converting the data to pandas dataframe
df = pd.DataFrame(data=data.data, columns=data.feature_names)

#displays first 5 rows
print(df.head())

# displays last 5 rows
print(df.tail())

# returns description of the data in the DataFrame
'''
count - The number of not-empty values.
mean - The average (mean) value.
std - The standard deviation.
min - the minimum value.
25% - The 25% percentile*.
50% - The 50% percentile*.
75% - The 75% percentile*.
max - the maximum value.

*Percentile meaning: how many of the values are less than the given percentile
'''
print(df.describe())

#describes about that particular column like it's name, the data type of the data it holds,..
print(df['sepal width (cm)'].describe())

#describes the data types of the entire dataframe
print(df.dtypes)

#to plot a heatmap
# heatmap - graphical representation of data that uses a system of color-coding to represent different values
# corr() - finds the correlation of each column in a DataFrame
# correlation - explains how one or more variables are related to each other
# annot = True, write the data value in each cell (ie, in heat map)
sns.heatmap(df.corr(), annot=True)  

# Positive correlation - A positive correlation exists when one variable decreases as the other variable decreases, or one variable increases while the other increases.
# in simple terms , variables are directly proportional to each other
sns.lmplot(x='petal width (cm)', y='petal length (cm)', data=df)

# Negative correlation - relationship between two variables such that as the value of one variable increases, the other decreases
# variables are inversely proportionally to each other
sns.lmplot(x='sepal width (cm)', y='petal length (cm)', data=df)