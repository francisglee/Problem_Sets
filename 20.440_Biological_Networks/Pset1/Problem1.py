# Problem Set 1: Probability Distributions and hypothesis testing 

# Problem 1A: Probability Distribution
# Write down the probability of finding AT_OCCURRENCE = 10 A's or T's bases in a window of S = 30 bases.  They can be non-consecutive.

import math

probability_dict = {} # key: value = Number of A's or T's: probability of occurrence

S = 30 # Sequence window length
AT_OCCURRENCE = 10 # Number of A's or T's

GC = .4 # GC probability
AT = .6 # AT probability

# figure out the probability of getting N number of A's or T's in sequence length, S
for ATcount in range(0, S + 1):
    if ATcount == 0:
        probability_dict[ATcount] = GC**S
    elif ATcount == 30:
        probability_dict[ATcount] = AT**S
    else:
        probability_dict[ATcount] = (GC**(30 - ATcount)) * (AT**ATcount) 

frequency_dict = {} # key: value = Number of A's or T's: possible frequency of occurrence
dict_size = len(probability_dict) 

# use pascals triangle to solve frequency for each number
def generate_pascals_triangle_lastrow(rows):
    """ Returns a list of the last row of a Pascal's Triangle with how many rows you want """
    triangle = [[1], [1, 1]]
    if rows == 1:
        return triangle[0]
    else:
        for row_number in range(2, rows):
            triangle.append([1] * row_number)
            for number in range(1, row_number):
                triangle[row_number][number] = (triangle[row_number - 1][number - 1] + triangle[row_number - 1][number])
            triangle[row_number].append(1)
        return triangle[-1]

# now find the frequency of each probability solved in probability_dict
for probability_dict_item in range(0, dict_size):
    if probability_dict_item == 0 or probability_dict_item == S:
        frequency_dict[probability_dict_item] = 1
    else:
        pascals = generate_pascals_triangle_lastrow(S + 1)
        frequency_dict[probability_dict_item] = pascals[probability_dict_item]

total_dict = {} # key: value = Number of A's or T's: total probability of occurrence

# Find total probability: P(total) = P(A) + P(B) + ... P(N)    
for x in range(0, dict_size):
    total_dict[x] = total_prob_recursion(probability_dict[x], frequency_dict[x])
    
# print results
# print "For sequence size of: ", S
# for key, value in probability_dict.items():
#     print "Number of AT: ", key, " has Probability: ", value

# for key, value in frequency_dict.items():
#     print "Number of AT: ", key, " has Frequency: ", value

total_sum = 0 # Counter for total probability; should equal 1

for key, value in total_dict.items():
    total_sum += value
    print "Number of AT:", key, "has Total Probability:", value

# validate probability distribution axioms
print "Total probability sums up to:", total_sum
# BOTH Exception and assert below don't work!
# if total_sum != 1:
#     raise Exception, "Your probabilities don't add up to 1!"
# assert total_sum == 1, "Your probabilities don't add up to 1!"
counter = 0
for N, probability in total_dict.items():
    if probability < 0:
        counter += 1
        raise Exception, "Your probabilities must be non-negative!"
if counter == 0:
    print "All probabilities are non-negative!"
        
print "The Probability of having", AT_OCCURRENCE, "A's or T's given:\n- Sequence window length of", S, "bp\n- GC probability of", GC, "\n- AT probability of", AT, "\nis:", total_dict[AT_OCCURRENCE]
