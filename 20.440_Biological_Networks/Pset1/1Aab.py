#!/usr/bin/env python
'''
Problem Set 1Aa, 1Ab: Probability Distributions and hypothesis testing 
What is the probability of finding theta = 10 A's or T's in a window of n = 30 bases?  They can be non-consecutive.
'''
import math 
import numpy as np

def poisson(k, n, theta):
    """returns poisson probability of k occurring at interval lamb (n * theta)"""
    lamb = n * theta
    return (lamb**k / math.factorial(k)) * np.exp(-lamb)

# define variables and parameters
n     = 30 # total number of trials (DNA sequence window of 30 bp)
theta = 0.6 # success probability; AT content
k     = 10 # desired success; number of AT desired

# SOLUTION
sltn_1Ab = poisson(k, n, theta)
print sltn_1Ab

# print solution
print "The poisson probability of finding", k, "As or Ts given:\n- Sequence window length:", n, "bp\n- AT content:", theta, "\nis:", sltn_1Ab
