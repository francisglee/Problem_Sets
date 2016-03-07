#!/usr/bin/env python
'''
Problem Set 1Ae: Probability Distributions and hypothesis testing 
Plot the full probability distribution for observing n[0:30] A or T bases in the n = 30 bp window.
'''
import math
import numpy as np
from matplotlib import pyplot as plt

%matplotlib inline

def poisson(k, n, theta):
    """returns poisson probability of k occurring at interval lamb (n * theta)"""
    lamb = n * theta
    return (lamb**k / math.factorial(k)) * np.exp(-lamb)

def poissondist(n, theta):
    """returns the poisson probability distribution list of k desired successes, out of n samples drawn, with theta success probability"""
    prob_list = [] # binomial distribution list
    for k in range(0, n + 1):  
        prob_list.append(poisson(k, n, theta))
    return prob_list

# define variables and parameters
n               = 30 # total number of trials (DNA sequence window of 30 bp)
theta           = 0.6 # success probability; AT content

# generate k_total set 
xval = np.arange(0, n + 1)

# generate binomial probability distribution set 
yval = poissondist(n, theta)

# plot binomial distribution(s)
plt.plot(xval, yval)

# format plot
plt.xlim(0, 30)
plt.ylim(0, 0.11)
plt.xlabel('Number of As and Ts')
plt.ylabel('Probability')
plt.title('Poisson Distribution')

plt.show()
