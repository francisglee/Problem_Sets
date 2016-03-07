#!/usr/bin/env python
'''
Problem Set 1B123: Model fitting and validation
-Using the data in data1B.mat divide it randomly into 10 equally sized groups, labeled k = 1, …, 10.
-For each value of k, hold out that partition of the data and fit polynomials for α = 1, 2, ..., 12 using the other data points not included in k. 
-Now compute the loss function using the data included in k that was not used for fitting. 
-When you are done, you should have 10 values of the loss function for each value of α. 

'''
from random import shuffle
import numpy as np
from matplotlib import pyplot as plt

%matplotlib inline

def equalpartition(x, y, k):
    """"randomly divides dataset into k parititions of equal size"""
    indexes = np.arange(0, len(x)) # create proxy index list
    shuffle(indexes) # shuffle indexes
    list_size = int(len(x) / k) # only works if list_size % k == 0!!!!!
    data_partitions = [] # return item
    for i in range(1, k + 1):
        start = list_size * (i - 1)
        end   = list_size * i
        xval  = x[start: end]
        yval  = y[start: end]
        data_partitions.append((xval, yval))    
    return data_partitions

def crosspartition(list):
    """returns k subsets of a dataset with k partitions, each subset containing a different k-1 combination of k-partitions
    :list: must contain k partitions, where each partition is (xvalues, yvalues)
    """
    # determine number of partitions in input list
    k = len(list)
    indexes = np.arange(0, k) # define index values for k partitions   
    cross_partitions_list = [] # define output object
    for index in indexes:
        # create identical temporary list 
        temp_list = [] 
        for item in list:
            temp_list.append(item)
        del temp_list[index] # remove partiton k
        x_val, y_val = [], [] # define c crosspartition subset
        for item in temp_list: 
            (x, y) = item
            for value in x: 
                x_val.append(value) # add remaining x values to c crosspartition subset
            for value in y:
                y_val.append(value) # add remaining y values to c crosspartition subset
        cross_partitions_list.append((x_val, y_val)) # add c crosspartition subset to cross_partitions_list
    return cross_partitions_list

def lossfunction(x, y, coefficient_list):
    """returns the prediction error of a model using values from coefficient_dict and an alpha value based on sample data, yrange"""
    loss = 0
    for index, item in enumerate(x):
        expected = np.polyval(coefficient_list, item)
        loss += (expected - y[index])**2
    return loss 

def mean(data):
    """return mean or expected value of a data"""
    return sum(data) / len(data)

# format data
data1AxIn = "-1.43700899917673	-1.41863578802289	-1.39860795267090	-1.38668022266832	-1.34003170017390	-1.32128129134871	-1.27724465353100	-1.24385072393791	-1.22178003711563	-1.18407163625350	-1.17015504113944	-1.13774310480797	-1.12887790538404	-1.12482960301584	-1.03598154686049	-0.954568343267126	-0.938716532038948	-0.930889907958599	-0.843924238839111	-0.816169663742941	-0.808114880921407	-0.762361004728118	-0.762242862876332	-0.754079307222671	-0.484110829674397	-0.452549303773177	-0.418376084363490	-0.409653537723603	-0.388192735582855	-0.366955578947159	-0.351007970776783	-0.304490215587930	-0.299723829475283	-0.281529348686641	-0.242672197555194	-0.235570024947647	-0.186364286052194	-0.171741659248361	-0.166936692521322	-0.155718658947313	-0.155503880593880	-0.126475253262615	-0.110762920957810	-0.0436043001064348	-0.0381488219701764	-0.0364794416256049	0.0163479545905116	0.0165515274760097	0.0513206032360689	0.0575972758963277	0.0618300990639535	0.0941367140852802	0.105985290400161	0.124737991200365	0.158882569767945	0.194228087986727	0.238688981993507	0.268300299220480	0.270788988841472	0.311801332676765	0.339001804085812	0.351510313334978	0.394293084934643	0.454034652942763	0.469129139141196	0.471656788985147	0.536077091019329	0.576036390304084	0.578861290750119	0.593589031207548	0.612317885325442	0.667701697566395	0.669287471297328	0.699734312196701	0.774867242090720	0.776426092193762	0.788513227307202	0.819858843261318	0.870404004714171	0.935610851118356	0.936534441794167	0.939288740893929	0.965670071543767	0.981782462660824	1.00917137565699	1.04027712546475	1.04458737579308	1.05824219819571	1.07875956972218	1.26101402886550	1.28490182136438	1.28622710701964	1.29969115915255	1.33075842432665	1.34819185383546	1.37385955558528	1.42134112506386	1.44106190855174	1.45145435202642	1.48259343277310"
data1Ax = map(float, data1AxIn.split('\t'))

data1AyIn = "2.08491985036798	1.73245809123114	2.41471486200074	2.19396205308547	2.56345281977010	2.44741165138425	2.87117806563201	3.11412037551951	3.43838046602547	3.01363765637096	3.58985006017174	2.67302156296364	3.73209625247395	3.59060610714399	4.09165858478678	4.21573149264147	3.89609128704814	3.20099536258769	4.57212118731595	5.02394241481935	3.05711195283901	4.14030495891103	4.94840671159386	4.08159897793531	5.75622974235380	4.27849865102608	5.04682290304648	5.58437609823673	5.04214054977244	4.68451892837110	4.98133588656933	4.31396128991347	4.45325346301853	5.28754301886976	5.45730409219217	5.95128396705237	4.45950646398403	4.91307246215535	4.73621478793225	5.48763128312492	5.30512796417796	5.41167165186497	4.86050783475363	4.72308396391348	4.66671620817874	4.74827701153906	4.77699354778241	5.55609887591343	5.16213407421075	5.63575972016253	5.28642593960147	4.36247370294163	4.61222178312629	4.35061470410438	5.38306456059680	5.44644012905085	5.23390973271697	5.18288873866677	5.21948083778518	4.33887803196259	5.32539832022348	4.86015862707399	5.38935381413068	6.02200812110559	4.70181495717045	5.33341594034088	6.42744359894970	5.12149965498088	5.44870750181180	5.48497865110176	4.96250021442624	5.18527364285294	5.69062420062930	5.58430876341443	5.90469687206277	5.13748939770317	4.43894697138323	5.18237553360777	5.16314706973154	5.63552710077402	6.04832995658845	6.07032471352556	5.92648256068429	6.06610108727346	5.33101975256839	5.92504472670441	6.08211283971614	6.74171042687329	6.60715618595117	7.14010405649456	6.90581729597582	6.05156548177625	7.81822062590477	7.50693681048638	7.99149110000779	7.49780280568150	7.16440513063133	8.04152652477001	8.51383249962180	7.81358393350853"
data1Ay = map(float, data1AyIn.split('\t'))

# define k partitions and c crosspartitions
k_partitions = equalpartition(data1Ax, data1Ay, 10)
[k1, k2, k3, k4, k5, k6, k7, k8, k9, k10] = k_partitions

k_crosspartitions = crosspartition(k_partitions)
[c1, c2, c3, c4, c5, c6, c7, c8, c9, c10] = k_crosspartitions # datasubsets (x, y) to move forward with cross validation

# fit polynomials for α = 1, 2, ..., 12 for c1 - c10
alpha = np.arange(1, 13) # define alpha list

# define coefficient dicts and list for each crosspartition
c1_coefficient_dict, c2_coefficient_dict, c3_coefficient_dict, c4_coefficient_dict, c5_coefficient_dict, c6_coefficient_dict, c7_coefficient_dict, c8_coefficient_dict, c9_coefficient_dict, c10_coefficient_dict = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, 

coefficient_dict_list = [
    c1_coefficient_dict, c2_coefficient_dict,
    c3_coefficient_dict, c4_coefficient_dict,
    c5_coefficient_dict, c6_coefficient_dict,
    c7_coefficient_dict, c8_coefficient_dict,
    c9_coefficient_dict, c10_coefficient_dict,
    ]

# define lossfunction dicts and lists for each crosspartition
c1_lossfunction_dict, c2_clossfunction_dict, c3_lossfunction_dict, c4_clossfunction_dict, c5_lossfunction_dict, c6_clossfunction_dict, c7_lossfunction_dict, c8_clossfunction_dict, c9_lossfunction_dict, c10_clossfunction_dict = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

lossfunction_dict_list = [
    c1_lossfunction_dict, c2_clossfunction_dict,
    c3_lossfunction_dict, c4_clossfunction_dict,
    c5_lossfunction_dict, c6_clossfunction_dict,
    c7_lossfunction_dict, c8_clossfunction_dict,
    c9_lossfunction_dict, c10_clossfunction_dict
    ]

# populate the coefficient dictionaries for values for each alpha
for index, item in enumerate(k_crosspartitions): # for each crosspartition
    for alpha_value in alpha: # across each alpha
        coefficient_dict_list[index][alpha_value]  = np.polyfit(item[0], item[1], alpha_value)
        lossfunction_dict_list[index][alpha_value] = lossfunction(item[0], item[1], coefficient_dict_list[index][alpha_value])
    
# calculate CV error for each alpha value, 
# where CV error is the average of all the loss functions for each alpha across the crosspartitions in k_crosspartitions
cv_error_dict = {} # define dict to store CV error 
for alpha_value in alpha:
    lossfunction_set = []
    for item in lossfunction_dict_list: # iterate through all loss function dicts
        lossfunction_set.append(item[alpha_value]) # collect all loss functions for alpha value
    cv_error_dict[alpha_value] = mean(lossfunction_set) # add loss function mean to cv_error_dict

# define y-values for cv_error  
cv_alpha = []
for item in alpha:
    cv_alpha.append(cv_error_dict[item])

# plot scatter
plt.scatter(alpha, cv_alpha)
plt.title('CV Error of crosspartition data vs alpha values')
plt.xlabel('alpha')
plt.ylabel('CV error')
plt.show()   

# print minimums for alpha
minimum = min(cv_alpha)
for index, item in enumerate(cv_alpha):
    if item == minimum:
        print "The alpha that minimizes CV error is:", alpha[index]
