from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Normal Distribution - probability distribution that is symmetric about the mean, 
# showing that data near the mean are more frequent in occurrence than data far from the mean 
# Graph - Bell shaped curve

# hist = False tells not to plot a histogram
#size indicates the sample size
sns.distplot(random.normal(size=1000), hist = False)
plt.title('Normal Distribution')
plt.show()


#Poisson distribution - probability distribution that is used to show how many times an event is likely to occur over a specified period.

# lam - Expected number of events occurring in a fixed-time interval, must be >= 0.
# kde - Whether to plot a gaussian kernel density estimate.

# EXTRAS
#gaussian kernel density estimate -  non-parametric way to estimate the probability density function of a random variable
#   Parametric statistics are based on assumptions about the distribution of population from which the sample was taken. 
#   Nonparametric statistics are not based on assumptions, that is, the data can be collected from a sample that does not follow a specific distribution.
#   Probability density function - probability distribution (the likelihood of an outcome) for a discrete random variable (e.g., a stock or ETF) as opposed to a continuous random variable.
#       Random variable - A random variable is a numerical description of the outcome of a statistical experiment
#           Discrete Random Variable - A discrete random variable is one which may take on only a countable number of distinct values such as 0,1,2,3,4,...
#A standard normal random variable is a normally distributed random variable with mean μ=0 and standard deviation σ=1.
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.title('Poisson Distribution')
plt.show()


#Chi Square Distribution - distribution of a sum of the squares of k independent standard normal random variables.

# EXTRAS
# independent standard normal random variables - sum of two independent normally distributed random variables is normal, 
#   with its mean being the sum of the two means, and its variance being the sum of the two variances

# df - Number of degrees of freedom, must be > 0.
# degrees of freedom - to decide whether there is a relation between the two variables in a population
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.title('Chi square Distribution')
plt.show()

#standard deviation is a measure of the amount of variation or dispersion of a set of values. A low standard deviation indicates that the values tend to be close to the mean of the set,
#while a high standard deviation indicates that the values are spread out over a wider range

#The variance measures the average degree to which each point differs from the mean
