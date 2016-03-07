#!/usr/bin/env python
'''
Problem Set 1B: Probability Distributions and hypothesis testing 
For each sample size N = [10, 100, 1000, 10000], randomly generate N samples from the distribution and use those values to estimate the mean. Repeat this process 1000 times, storing the means for each of the 4*1,000 samples. Plot a box-plot of the mean values for each value of N.
'''
import math
import numpy as np
from matplotlib import pyplot as plt

%matplotlib inline

# define parameters for normal distribution
mean  = 5 # true mean
stdev = 5 # standard deviation

N = [10, 100, 1000, 10000] # list of sample sizes

ten, hundred, thousand, ten_thousand = [], [], [], [] # values from random sampling

# random sampling from a normal distribution
for int in range(0, 1000): # repeat 1000X
    for index, sample_size in enumerate(N):
        sampling = np.random.normal(mean, stdev, sample_size) 
        if index == 0:
            ten.extend(sampling)
        elif index == 1:
            hundred.extend(sampling)
        elif index == 2:
            thousand.extend(sampling)
        else:
            ten_thousand.extend(sampling)
        
data = [ten, hundred, thousand, ten_thousand]

# Plot box-plots for each sample size in N
fig = plt.figure()
ax = fig.add_subplot(111)

plt.boxplot(data, labels = N, showmeans = True)

# format plot
fig.suptitle('Mean Value for Various Sample Sizes', fontsize=14, fontweight='bold')
ax.set_xlabel('Sample Size')
ax.set_ylabel('Values')

plt.show()
