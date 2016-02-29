# Problem Set 1A: Probability Distributions and hypothesis testing 

# What is the probability of finding AT_OCCURRENCE = 10 A's or T's bases in a window of S = 30 bases?  They can be non-consecutive.
# What is the probability of finding AT_OCCURRENCE <= 10 A's or T's bases in the same window?
# What is the probability of finding 10 <= AT_OCCURRENCE <= 15 A's or T's bases in the same window?
# Plot the full probability distribution for observing 0:30 A or T bases in the 30 base window.

%matplotlib inline

import math 
import numpy as np
from matplotlib import pyplot as plt

# binomial coefficient
N = 30
THETA = 0.6

# parameters
AT_OCCURRENCE = 10
SPREAD = [10, 15]

def bin(N, THETA):
    """returns the binomial distribution Mass distribution for items in N"""
    bin_list = [] # distribution list 
    for x in range(0, N + 1):
        # issues with long
        temp1 = math.factorial(N)
        temp2 = math.factorial(x)
        temp3 = math.factorial(N-x)
        binomial_coefficient = temp1/(temp2 * temp3)
        bin_list.append(binomial_coefficient * (THETA**x) * (1-THETA)**(N-x))
    return bin_list

pmf = bin(N, THETA) # probability mass function distribution; also yrange

# print results
# for item in pmf:
#     print "n =", pmf.index(item), ", P(n) =", item

# validate probability distribution axioms
total_sum = 0
for element in pmf:
    total_sum += element
if total_sum == 1:
    print "Total probability sums up to:", total_sum
else: # TODO: This is broken
    print "Total probability sums up to:", total_sum, "\nIt needs to be 1.0" 
# BOTH Exception and assert below don't work!
# if total_sum != 1:
#     raise Exception, "Your probabilities don't add up to 1!"
# assert total_sum == 1, "Your probabilities don't add up to 1!"
counter = 0
for element in pmf:
    if element < 0:
        counter += 1
if counter == 0:
    print "All probabilities are non-negative!"
else:
    print "You cannot have negative probabilities :("

# single variable solution
print "\nThe Probability of having", AT_OCCURRENCE, "A's or T's given:\n- Sequence window length of", N, "bp\n- GC probability of", 1 - THETA, "\n- AT probability of", THETA, "\nis:", pmf[AT_OCCURRENCE]

# cumulative distribution function (CDF)
cdf = 0
for x in range(0, AT_OCCURRENCE + 1):
    cdf += pmf[x]
print "\nThe Probability of having at most", AT_OCCURRENCE, "A's or T's given:\n- Sequence window length of", N, "bp\n- GC probability of", 1 - THETA, "\n- AT probability of", THETA, "\nis:", cdf

# spread distribution
spread_probability = 0
for x in range(SPREAD[0], SPREAD[1] + 1):
    spread_probability += pmf[x]
print "\nThe Probability of having between (inclusive)", SPREAD[0], "and", SPREAD[1], "A's or T's given:\n- Sequence window length of", N, "bp\n- GC probability of", 1 - THETA, "\n- AT probability of", THETA, "\nis:", spread_probability

# Define the distribution parameters to be plotted
x = np.arange(0, 31)

# plot binomial distribution
plt.plot(x, pmf)

plt.xlim(0, 35)
plt.ylim(0, 0.20)

plt.xlabel('Number of As and Ts')
plt.ylabel('Probability')
plt.title('Binomial Distribution')

plt.show()
