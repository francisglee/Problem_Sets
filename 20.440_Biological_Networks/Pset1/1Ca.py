#!/usr/bin/env python
'''
Problem Set 1Ca: Probability Distributions and hypothesis testing 
Manually approximate the probability of drawing 3 or more red marbles from a bag of 10 marbles, 4 of which are red, using the binomial distribution.
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

# define parameters for binomial distribution
n     = 4 # total number of marbles drawn           
theta = 0.4 # success probability of picking red marble from bag
k_set = [3, 4] # desired successes; we want >= 3 red marbles and there's 4 total red marbles

# define solution
sltn_1Ca = 0

# find binomial probabilities of k_set
for item in k_set:
    sltn_1Ca += binomial(n, item, theta)
    
# print results
print "The binomial probability of drawing", k_set[0], "to", k_set[-1], "red marbles from a bag given:\n- Total number of marbles: 10\n- Total number of red marbles: 4\nis:", sltn_1Ca
