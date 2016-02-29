# Problem Set 1: Probability Distributions and hypothesis testing 

# Problem 1A: Probability Distribution
# Write down the probability of finding AT_OCCURRENCE = 10 A's or T's bases in a window of N = 30 bases.  They can be non-consecutive.

import math

# binomial coefficient
N = 30
THETA = 0.6

AT_OCCURRENCE = 10

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

pmf = bin(N, THETA)

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
        
print "The Probability of having", AT_OCCURRENCE, "A's or T's given:\n- Sequence window length of", N, "bp\n- GC probability of", 1 - THETA, "\n- AT probability of", THETA, "\nis:", pmf[AT_OCCURRENCE]

