#!/usr/bin/env python
'''
Problem Set 2Bb: Probability Distributions and hypothesis testing 
Use the fitdist (MATLAB) function to fit the data to each of these six probability distributions: 
- Exponential 
- Poisson 
- Normal 
- Negative Binomial
- Logistic 
- Weibull. (using double Weibull)
'''
import numpy as np
from scipy.misc import factorial
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

%matplotlib inline

# Generate some data for this demonstration.
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
    256, 237, 381, 156, 272, 356, 643, 572, 159, 217
    ]

# poisson function, parameter lamb is the fit parameter
def poisson(k, lamb): # keeps passing 1.0 for lamb, doesn't try enough lamb values
    return (lamb**k / factorial(k)) * np.exp(-lamb)



# Plot the histogram.
entries, bin_edges, patches = plt.hist(data2B, bins = 25, normed = True, alpha = 0.6, color = 'grey')

# Generate x_val
xmin, xmax = min(data2B), max(data2B) # xmin, xmax = plt.xlim()
x_val = np.linspace(xmin, xmax, len(data2B)) # x_val = np.linspace(xmin, xmax, 1000)
x_val_poisson = np.linspace(xmin, xmax, xmax - xmin + 1) # x_val = np.linspace(xmin, xmax, 1000)
print x_val_poisson
bin_middles = 0.5*(bin_edges[1:] + bin_edges[:-1]) # x values for curve fits

# Fit distribution to the data and evaluate parameters:
mu_norm, std_norm                         = stats.norm.fit(data2B)
mu_expon, std_expon                       = stats.expon.fit(data2B)
mu_logistic, std_logistic                 = stats.logistic.fit(data2B)
mu_dweibull, std_dweibull, shape_dweibull = stats.dweibull.fit(data2B)
# parameters_poisson, cov_matrix_poisson    = curve_fit(poisson, x_val_poisson, entries, check_finite = True)
print len(parameters_poisson), type(parameters_poisson), parameters_poisson[0] 
print len(cov_matrix_poisson), type(cov_matrix_poisson), cov_matrix_poisson, "END"

# Generate y_val for each distribution
pdf_norm     = stats.norm.pdf(x_val, mu_norm, std_norm)
pdf_expon    = stats.expon.pdf(x_val, mu_expon, std_expon) 
pdf_logistic = stats.logistic.pdf(x_val, mu_logistic, std_logistic) 
pdf_dweibull = stats.dweibull.pdf(x_val, mu_dweibull, std_dweibull, shape_dweibull)
# pmf_poisson  = poisson(x_val, *parameters_poisson)
# pmf_binom    =

# plot distributions
plt.plot(x_val, pdf_norm, color = 'black', linewidth = 2, label = "Normal")
plt.plot(x_val, pdf_expon, 'y--', linewidth = 2, label = "Exponential")
plt.plot(x_val, pdf_logistic, 'b:', linewidth = 2, label = "Logistic")
plt.plot(x_val, pdf_dweibull, 'r-', linewidth = 2, label = "Weibull") 
# plt.plot(x_val, pmf_poisson, 'g+', linewidth = 2, label = "Poisson")
# plt.plot(x_val, pmf_binom, 'k.', linewidth = 2, label = "Negative Binomial")

# Add labels, titles, legends
plt.title("Fitting data2B to six probability distributions")
plt.ylabel("Probability")
plt.xlabel("Numbers")
plt.legend(loc = 'upper right')

plt.show()
