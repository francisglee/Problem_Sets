#!/usr/bin/env python
'''
Problem Set 1Cd: Probability Distributions and hypothesis testing 
For each of the background sizes in (c) above, also plot the probability densities over the range [0 4] (for drawing between 0 and 4 red marbles) for both the binomial and hypergeometric distributions.
'''
import math 
import numpy as np
from matplotlib import pyplot as plt

%matplotlib inline

def choose(n, k):
    """returns n choose k: n!/(k!(n - k)!)"""
    f = math.factorial
    return f(n) / f(k) / f(n - k)

def binomial(n, k, theta):
    """returns the binomial probability of k desired success, out of n samples drawn, with theta success probability"""
    return choose(n, k) * (theta**k) * (1 - theta)**(n - k) # choose(n, k) = binomial_coefficient

def binomialdist(n, theta):
    """returns the binomial probability distribution list of k desired successes, out of n samples drawn, with theta success probability"""
    bin_list = [] # binomial distribution list
    for k in range(0, n + 1):  
        bin_list.append(binomial(n, k, theta))
    return bin_list

def hypergeo(K, N, n, k):
    """returns the hypergeometric probability of k success, out of n samples drawn, given N total samples and K success samples"""
    a = choose(K, k)
    b = choose(N - K, n - k)
    c = choose(N, n)
    return float((a * b))/c

def hypergeodist(K, N, n):
    """returns the hypergeometric probability distribution list of k success, out of n samples drawn, given N total samples and K success samples"""
    dist_list = [] 
    for k in range(0, n + 1):  
        dist_list.append(hypergeo(K, N, n, k))
    return dist_list

# define global variables
theta = 0.4 # probability of drawing a red marble from bag
n     = 4 # samples drawn
k     = [3, 4] # number of desired marbles grabbed from each draw

# define background sizes: [N, K] where N is number of total marbles, and K is the total number of red marbles
background_dict = {
    'alpha'   : [10, 4],
    'beta'    : [50, 20],
    'gamma'   : [100, 40],
    'delta'   : [1000, 400],
    'epsilon' : [5000, 2000],
    'zeta'    : [10000, 4000]
    }

# define hypergeometric probability distribution dictionary 
hypergeo_probability_dict = {}

# calculate binomial probability distribution
bin_probability_list = binomialdist(n, theta)

# calculate hypergeometric probability distribution and store them in probabiliity_dict
for key, value in background_dict.items():
    hypergeo_probability_dict[key] = hypergeodist(value[1], value[0], n)

# define data for binomial and hypergeometric mass function plots 
xrange = np.arange(0, n + 1, 1) # x values for all plots
# bin_probability_list = binomial y values
# hypergeo_probability_dict['alpha'] = hypergeometric y values for sample size = 10
# hypergeo_probability_dict['beta'] = hypergeometric y values for sample size = 50
# hypergeo_probability_dict['gamma'] = hypergeometric y values for sample size = 100
# hypergeo_probability_dict['delta'] = hypergeometric y values for sample size = 1000
# hypergeo_probability_dict['epsilon'] = hypergeometric y values for sample size = 5000
# hypergeo_probability_dict['zeta'] = hypergeometric y values for sample size = 10000

# define figures for plots
fig, ax = plt.subplots(3, 2, figsize = [16, 12], sharex = True, sharey = True)

ax[0,0].plot(xrange, hypergeo_probability_dict['alpha'], 'r-', label = 'hypergeometric')
ax[0,1].plot(xrange, hypergeo_probability_dict['beta'], 'r-', label = 'hypergeometric')
ax[1,0].plot(xrange, hypergeo_probability_dict['gamma'], 'r-', label = 'hypergeometric')
ax[1,1].plot(xrange, hypergeo_probability_dict['delta'], 'r-', label = 'hypergeometric')
ax[2,0].plot(xrange, hypergeo_probability_dict['epsilon'], 'r-', label = 'hypergeometric')
ax[2,1].plot(xrange, hypergeo_probability_dict['zeta'], 'r-', label = 'hypergeometric')

ax[0,0].plot(xrange, bin_probability_list, 'b--', label = 'binomial')
ax[0,1].plot(xrange, bin_probability_list, 'b--', label = 'binomial')
ax[1,0].plot(xrange, bin_probability_list, 'b--', label = 'binomial')
ax[1,1].plot(xrange, bin_probability_list, 'b--', label = 'binomial')
ax[2,0].plot(xrange, bin_probability_list, 'b--', label = 'binomial')
ax[2,1].plot(xrange, bin_probability_list, 'b--', label = 'binomial')

# Add titles
fig.suptitle("Hypergeometric distributions converges with Binomial distributions at larger sample sizes", fontsize = 25)
ax[0,0].set_title("Sample Size = 10")
ax[0,1].set_title("Sample Size = 50")
ax[1,0].set_title("Sample Size = 100")
ax[1,1].set_title("Sample Size = 1000")
ax[2,0].set_title("Sample Size = 5000")
ax[2,1].set_title("Sample Size = 10000")

# Add axes labels
fig.text(0.5, 0.01, 'Number of red marbles drawn', ha = 'center', fontsize = 25)
fig.text(0.04, 0.5, 'Probability', va='center', rotation = 'vertical', fontsize = 25)

# Add legend
plt.legend(loc = 'upper right', bbox_to_anchor=(0.1, -0.1))

# format figure
fig.subplots_adjust(hspace = 0.2) 
plt.xticks(xrange)

plt.show()
