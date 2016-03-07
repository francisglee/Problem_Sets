#!/usr/bin/env python
'''
Problem Set 2Ba: Probability Distributions and hypothesis testing 
Load the data in the file data2B.mat and visualize the raw data. To load the data, use load(‘data2B.mat’) which will load the data as a vector titled ‘data2B’. The hist function will also be useful for visualizing the data.
'''
import matplotlib.pyplot as plt

%matplotlib inline

data2B = [
    59, 449, 209, 405, 207, 304, 632, 492, 422, 55,
    49, 527, 401, 633, 115, 73, 241, 240, 379, 363,
    65, 126, 386, 100, 117, 100, 244, 69, 278, 423,
    247, 326, 301, 333, 403, 179, 360, 501, 169, 21,
    388, 428, 325, 127, 42, 387, 163, 153, 291, 707,
    290, 454, 226, 322, 503, 276, 58, 114, 440, 495,
    307, 180, 349, 227, 176, 338, 212, 166, 177, 534,
    330, 281, 286, 136, 601, 179, 307, 296, 250, 598,
    62, 326, 190, 226, 217, 242, 201, 292, 316, 216,
    419, 905, 150, 362, 150, 329, 499, 401, 75, 168,
    355, 116, 54, 227, 476, 158, 332, 162, 110, 269,
    116, 171, 212, 188, 302, 92, 234, 376, 174, 208, 
    508, 303, 151, 284, 404, 181, 327, 148, 435, 284,
    233, 160, 163, 441, 219, 556, 396, 224, 119, 293, 
    669, 213, 328, 89, 227, 720, 179, 690, 309, 517,
    241, 582, 317, 87, 207, 288, 138, 379, 381, 220,
    351, 150, 56, 107, 357, 239, 565, 486, 278, 127,
    209, 206, 542, 97, 243, 176, 190, 155, 379, 364,
    581, 330, 421, 283, 330, 232, 354, 293, 305, 363,
    256, 237, 381, 156, 272, 356, 643, 572, 159, 217]

# Plot histogram of data2B
entries, bin_edges, c = plt.hist(data2B, normed = True)
plt.title("data2B")
plt.ylabel("Frequency")
plt.xlabel("Data Numbers")

plt.show()
print sum(entries)
