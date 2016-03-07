#!/usr/bin/env python
'''
Problem Set 1Cc: Probability Distributions and hypothesis testing 
Demonstrate the convergence of the hypergeometric distribution to the binomial distribution as background size increases by calculating with the hygecdf function in Matlab the probability of drawing 3 or more red marbles in 4 tries from a bag containing:
   10 marbles, of which 4 are red
   50 marbles, of which 20 are red
  100 marbles, of which 40 are red
 1000 marbles, of which 400 are red
 5000 marbles, of which 2000 are red
10000 marbles, of which 4000 are red
'''
import math 
import numpy as np

def choose(n, k):
    """returns n choose k: n!/(k!(n - k)!)"""
    f = math.factorial
    return f(n) / f(k) / f(n - k)

def binomial(n, k, theta):
    """returns the binomial probability of k desired success, out of n samples drawn, with theta success probability"""
    return choose(n, k) * (theta**k) * (1 - theta)**(n - k) # choose(n, k) = binomial_coefficient

def hypergeo(K, N, n, k):
    """returns the hypergeometric probability of k success, out of n samples drawn, given N total samples and K success samples"""
    a = choose(K, k)
    b = choose(N - K, n - k)
    c = choose(N, n)
    return float((a * b))/c

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

# define probability values 
hypergeo_probability_dict = {}

# determine binomial probabilities 
binomial_prob = binomial(n, k[0], theta) + binomial(n, k[1], theta)

# determine hypergeometric probabilities and store them in probabiliity_dict
for key, value in background_dict.items():
    hypergeo_prob_start = hypergeo(value[1], value[0], n, k[0])
    hypergeo_prob_end = hypergeo(value[1], value[0], n, k[1]) 
    hypergeo_prob = hypergeo_prob_end + hypergeo_prob_start
    hypergeo_probability_dict[key] = hypergeo_prob 
    
# print results
for key, value in hypergeo_probability_dict.items():
    print "A sample size of", background_dict[key][0], "has a hypergeometric probability of", value
print "The binomial probability is", binomial_prob
