#!/usr/bin/env python
'''
Problem Set 2Aa: Probability Distributions and hypothesis testing 
Plot a Q-Q plot comparing each of the cases below to the Normal distribution:
-1000 points sampled from a Normal distribution with mean equal to 0 and standard deviation equal to 1.
-10 points sampled from a Normal distribution with mean equal to 0 and standard deviation equal to 1.
-100 points sampled from a Binomial distribution with p = 0.5.
-1000 points sampled from a Binomial distribution with p = 0.5.
-1000 points sampled from a uniform distribution between -1 and 1.
-1000 points where the first 500 are drawn from a Normal distribution with mean equal to 5 and standard deviation equal to 1 and where the second 500 are drawn from a Normal distribution with mean equal to 10 and standard deviation equal to 2.
'''
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

%matplotlib inline

# define dicts for each collection and place in list
collectn_a, collectn_b, collectn_c, collectn_d, collectn_e, collectn_f = {}, {}, {}, {}, {}, {}
collectn = [collectn_a, collectn_b, collectn_c, collectn_d, collectn_e, collectn_f] 

# generate data off of a normal distribution
collectn_a['data'] = np.random.normal(0, 1, 1000).tolist() # mean, stdev, number of samples
collectn_b['data'] = np.random.normal(0, 1, 10).tolist() 
collectn_f['data'] = np.random.normal(5, 1, 500).tolist() + np.random.normal(10, 2, 500).tolist()

# generate data off of a binomial distribution with n = 10 assumption
collectn_c['data'] = np.random.binomial(10, 0.5, 100).tolist() # trial size, success probability, number of samples 
collectn_d['data'] = np.random.binomial(10, 0.5, 1000).tolist()

# generate data off of a uniform distribution
collectn_e['data'] = np.random.uniform(-1, 1, 1000).tolist() # min, max, sampling size

# for each collection, Calculate quantiles and least-square-fit curve
for item in collectn:
    (quantiles, values), (slope, intercept, r) = stats.probplot(item['data'], dist = 'norm')
    item['quantiles'] = quantiles.tolist()
    item['values']    = values.tolist()
    item['slope']     = slope
    item['intercept'] = intercept
    item['r']         = r

# convert quantiles back to ndarray so they can be computed below... dunno if there's a better fix, probably
for item in collectn:
    temp  = item['quantiles']    
    item['quantiles'] = np.array(temp)

# define figure and axes
fig, ax = plt.subplots(3, 2, figsize = [16, 12])

ax_list = [ax[0, 0], ax[0, 1], ax[1, 0], ax[1, 1], ax[2, 0], ax[2, 1]]

# plot QQ-plots 
ax[0,0].plot(collectn_a['values'], collectn_a['quantiles'], 'ob', collectn_a['quantiles'] * collectn_a['slope'] + collectn_a['intercept'], collectn_a['quantiles'], 'r')
ax[0,1].plot(collectn_b['values'], collectn_b['quantiles'], 'ob', collectn_b['quantiles'] * collectn_b['slope'] + collectn_b['intercept'], collectn_b['quantiles'], 'r')
ax[1,0].plot(collectn_c['values'], collectn_c['quantiles'], 'ob', collectn_c['quantiles'] * collectn_c['slope'] + collectn_c['intercept'], collectn_c['quantiles'], 'r')
ax[1,1].plot(collectn_d['values'], collectn_d['quantiles'], 'ob', collectn_d['quantiles'] * collectn_d['slope'] + collectn_d['intercept'], collectn_d['quantiles'], 'r')
ax[2,0].plot(collectn_e['values'], collectn_e['quantiles'], 'ob', collectn_e['quantiles'] * collectn_e['slope'] + collectn_e['intercept'], collectn_e['quantiles'], 'r')
ax[2,1].plot(collectn_f['values'], collectn_f['quantiles'], 'ob', collectn_f['quantiles'] * collectn_f['slope'] + collectn_f['intercept'], collectn_f['quantiles'], 'r')

# Add titles
fig.suptitle("Q-Q plots against a Normal distribution", fontsize = 25)
ax[0,0].set_title("1000 samples from a Normal distribution\nmean = 0, stdev = 1")
ax[0,1].set_title("10 samples from a Normal distribution\nmean = 0, stdev = 1")
ax[1,0].set_title("100 samples from a Binomial distribution\nn = 10, p = 0.5")
ax[1,1].set_title("1000 samples from a Binomial distribution\nn = 10, p = 0.5")
ax[2,0].set_title("1000 samples from a Uniform distribution\nmin = -1, max = 1")
ax[2,1].set_title("1000 samples from a normal distribution\nmean = 5 (500 samples), 10 (500 samples)\n stdev = 1 (500 samples), 2 (500 samples)")

# Add axes labels
fig.text(0.5, 0.01, 'Sample Quantiles', ha = 'center', fontsize = 25)
fig.text(0.04, 0.5, 'Probability', va='center', rotation = 'vertical', fontsize = 25)

#define ticks
ticks_perc = [0.3, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0, 75.0, 90.0, 95.00, 98.00, 99.0, 99.7]

#transfrom them from precentile to cumulative density
ticks_quan = [stats.norm.ppf(i / 100.) for i in ticks_perc]

# for all graphs and add grids and new ticks for all graphs
for graph in ax_list:
    graph.grid()
    graph.set_yticks(ticks_quan)
    graph.set_yticklabels(ticks_perc)
    
# format figure
fig.subplots_adjust(hspace = 0.5) 

# show plot
plt.show()
