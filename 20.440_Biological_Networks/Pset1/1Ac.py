#!/usr/bin/env python
'''
Problem Set 1Ac: Probability Distributions and hypothesis testing 
What is the probability of finding theta <= 10 A's or T's bases in the same window (n = 30)?
'''
import math 
import numpy as np

def poisson(k, n, theta):
    """returns poisson probability of k occurring at interval lamb (n * theta)"""
    lamb = n * theta
    return (lamb**k / math.factorial(k)) * np.exp(-lamb)

def poissoncdf(k, n, theta): # assumes 0 for k_min!!!
    """returns the poisson cumulative distribution list of range(0, k) of desired successes, out of n samples drawn, with theta success probability"""
    prob_list = [] # binomial distribution list
    for x in range(0, k + 1):  
        probability = poisson(x, n, theta) # x is k in k_range
        prob_list.append(probability)
    return sum(prob_list)

# define variables and parameters
n        = 30 # total number of trials (DNA sequence window of 30 bp)
theta    = 0.6 # success probability; AT content
k        = 10 # max desired success value 
    
# SOLUTION
sltn_1Ac = poissoncdf(k, n, theta)

# print solution
print "The poisson probability of finding", k, "or less As or Ts given:\n- Sequence window length:", n, "bp\n- AT content:", theta, "\nis:", sltn_1Ac
