#!/usr/bin/env python
'''
Problem Set 1A8: Model fitting and validation
-To further assess the appropriate α value, repeat steps (2)-(5) 20 times for all α values. 
-Store the MSE values for all α x 20 fits and plot the mean training and validation errors on a single plot. 
-Determine the optimal α value following this procedure and comment on whether or not the result here is the same as in (5)
'''
from random import shuffle
import numpy as np
from matplotlib import pyplot as plt

%matplotlib inline

def datapartition(x, y, training, validation, assessment):
    '''Returns an randomly selected training, validation, and assessment data partitions from data
    :training: fraction of data partitioned for training
    :validation: fraction of data partitioned for validation
    :assessment: fraction of data partitioned for assessment
    '''
    indexes = np.arange(0, len(x)) # create proxy index list
    
    # create sizes for each partition
    training_size   = int(len(x) * training) # only works if len(x) % 2 == 0!!!
    validation_size = int(len(x) * validation) # only works if len(x) % 2 == 0!!! 
    
    shuffle(indexes) # shuffle indexes
    
    randomized_training_index   = indexes[0: training_size]
    randomized_validation_index = indexes[training_size: training_size + validation_size]
    randomized_assessment_index = indexes[training_size + validation_size:]
    
    training_set_x, training_set_y = [], []
    for item in randomized_training_index:
        training_set_x.append(x[item])
        training_set_y.append(y[item])    
    
    validation_set_x, validation_set_y = [], []
    for item in randomized_validation_index:
        validation_set_x.append(x[item])
        validation_set_y.append(y[item])
    
    assessment_set_x, assessment_set_y = [], []
    for item in randomized_validation_index:
        assessment_set_x.append(x[item])
        assessment_set_y.append(y[item])
    
    return (training_set_x, training_set_y), (validation_set_x, validation_set_y), (assessment_set_x, assessment_set_y)

def lossfunction(x, y, coefficient_list):
    """returns the prediction error of a model using values from coefficient_dict and an alpha value based on sample data, yrange"""
    loss = 0
    for index, item in enumerate(x):
        expected = np.polyval(coefficient_list, item)
        loss += (expected - y[index])**2
    return loss 

def mse(x, y, coefficient_list):
    """returns the mean squared error of data"""
    return lossfunction(x, y, coefficient_list) / len(x)

def mean(data):
    """return mean or expected value of a data"""
    return sum(data) / len(data)

# format data
data1AxIn = "-1.43700899917673	-1.41863578802289	-1.39860795267090	-1.38668022266832	-1.34003170017390	-1.32128129134871	-1.27724465353100	-1.24385072393791	-1.22178003711563	-1.18407163625350	-1.17015504113944	-1.13774310480797	-1.12887790538404	-1.12482960301584	-1.03598154686049	-0.954568343267126	-0.938716532038948	-0.930889907958599	-0.843924238839111	-0.816169663742941	-0.808114880921407	-0.762361004728118	-0.762242862876332	-0.754079307222671	-0.484110829674397	-0.452549303773177	-0.418376084363490	-0.409653537723603	-0.388192735582855	-0.366955578947159	-0.351007970776783	-0.304490215587930	-0.299723829475283	-0.281529348686641	-0.242672197555194	-0.235570024947647	-0.186364286052194	-0.171741659248361	-0.166936692521322	-0.155718658947313	-0.155503880593880	-0.126475253262615	-0.110762920957810	-0.0436043001064348	-0.0381488219701764	-0.0364794416256049	0.0163479545905116	0.0165515274760097	0.0513206032360689	0.0575972758963277	0.0618300990639535	0.0941367140852802	0.105985290400161	0.124737991200365	0.158882569767945	0.194228087986727	0.238688981993507	0.268300299220480	0.270788988841472	0.311801332676765	0.339001804085812	0.351510313334978	0.394293084934643	0.454034652942763	0.469129139141196	0.471656788985147	0.536077091019329	0.576036390304084	0.578861290750119	0.593589031207548	0.612317885325442	0.667701697566395	0.669287471297328	0.699734312196701	0.774867242090720	0.776426092193762	0.788513227307202	0.819858843261318	0.870404004714171	0.935610851118356	0.936534441794167	0.939288740893929	0.965670071543767	0.981782462660824	1.00917137565699	1.04027712546475	1.04458737579308	1.05824219819571	1.07875956972218	1.26101402886550	1.28490182136438	1.28622710701964	1.29969115915255	1.33075842432665	1.34819185383546	1.37385955558528	1.42134112506386	1.44106190855174	1.45145435202642	1.48259343277310"
data1Ax   = map(float, data1AxIn.split('\t'))

data1AyIn = "2.08491985036798	1.73245809123114	2.41471486200074	2.19396205308547	2.56345281977010	2.44741165138425	2.87117806563201	3.11412037551951	3.43838046602547	3.01363765637096	3.58985006017174	2.67302156296364	3.73209625247395	3.59060610714399	4.09165858478678	4.21573149264147	3.89609128704814	3.20099536258769	4.57212118731595	5.02394241481935	3.05711195283901	4.14030495891103	4.94840671159386	4.08159897793531	5.75622974235380	4.27849865102608	5.04682290304648	5.58437609823673	5.04214054977244	4.68451892837110	4.98133588656933	4.31396128991347	4.45325346301853	5.28754301886976	5.45730409219217	5.95128396705237	4.45950646398403	4.91307246215535	4.73621478793225	5.48763128312492	5.30512796417796	5.41167165186497	4.86050783475363	4.72308396391348	4.66671620817874	4.74827701153906	4.77699354778241	5.55609887591343	5.16213407421075	5.63575972016253	5.28642593960147	4.36247370294163	4.61222178312629	4.35061470410438	5.38306456059680	5.44644012905085	5.23390973271697	5.18288873866677	5.21948083778518	4.33887803196259	5.32539832022348	4.86015862707399	5.38935381413068	6.02200812110559	4.70181495717045	5.33341594034088	6.42744359894970	5.12149965498088	5.44870750181180	5.48497865110176	4.96250021442624	5.18527364285294	5.69062420062930	5.58430876341443	5.90469687206277	5.13748939770317	4.43894697138323	5.18237553360777	5.16314706973154	5.63552710077402	6.04832995658845	6.07032471352556	5.92648256068429	6.06610108727346	5.33101975256839	5.92504472670441	6.08211283971614	6.74171042687329	6.60715618595117	7.14010405649456	6.90581729597582	6.05156548177625	7.81822062590477	7.50693681048638	7.99149110000779	7.49780280568150	7.16440513063133	8.04152652477001	8.51383249962180	7.81358393350853"
data1Ay   = map(float, data1AyIn.split('\t'))

# define global mse_dicts for training and validation for 20 iterations
mse_dict_training1, mse_dict_training2, mse_dict_training3, mse_dict_training4, mse_dict_training5, mse_dict_training6, mse_dict_training7, mse_dict_training8, mse_dict_training9, mse_dict_training10, mse_dict_training11, mse_dict_training12, mse_dict_training13, mse_dict_training14, mse_dict_training15, mse_dict_training16, mse_dict_training17, mse_dict_training18, mse_dict_training19, mse_dict_training20 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} 
mse_dict_validation1, mse_dict_validation2, mse_dict_validation3, mse_dict_validation4, mse_dict_validation5, mse_dict_validation6, mse_dict_validation7, mse_dict_validation8, mse_dict_validation9, mse_dict_validation10, mse_dict_validation11, mse_dict_validation12, mse_dict_validation13, mse_dict_validation14, mse_dict_validation15, mse_dict_validation16, mse_dict_validation17, mse_dict_validation18, mse_dict_validation19, mse_dict_validation20 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}     

mse_dict_training_list = [
    mse_dict_training1, mse_dict_training2,
    mse_dict_training3, mse_dict_training4,
    mse_dict_training5, mse_dict_training6,
    mse_dict_training7, mse_dict_training8,
    mse_dict_training9, mse_dict_training10,
    mse_dict_training11, mse_dict_training12,
    mse_dict_training13, mse_dict_training14,
    mse_dict_training15, mse_dict_training16,
    mse_dict_training17, mse_dict_training18,
    mse_dict_training19, mse_dict_training20,
    ]

mse_dict_validation_list = [
    mse_dict_validation1, mse_dict_validation2,
    mse_dict_validation3, mse_dict_validation4,
    mse_dict_validation5, mse_dict_validation6,
    mse_dict_validation7, mse_dict_validation8,
    mse_dict_validation9, mse_dict_validation10,
    mse_dict_validation11, mse_dict_validation12,
    mse_dict_validation13, mse_dict_validation14,
    mse_dict_validation15, mse_dict_validation16,
    mse_dict_validation17, mse_dict_validation18,
    mse_dict_validation19, mse_dict_validation20
    ]

# repeat the assessment 20 times
for trial in range(0, 20):
    # create training, validation, and assessment datasets from data1Ax, data1Ay
    training, validation, assessment = datapartition(data1Ax, data1Ay, 0.5, 0.25, 0.25)

    # define dicts and lists for coefficients and evalations
    alpha = np.arange(1, 13) # problem set specific
    coefficient_dict_training = {}

    for a in range(1, len(alpha) + 1): # store these values in global mse dicts
        coefficient_dict_training[a] = np.polyfit(training[0], training[1], a)
        mse_dict_training_list[trial][a] = mse(training[0], training[1], coefficient_dict_training[a])
        mse_dict_validation_list[trial][a] = mse(validation[0], validation[1], coefficient_dict_training[a])

    # find alpha of lowest MSE for each training and validation set 
    alpha_min_tra, alpha_min_val = 0, 0 # define variables
    for key, value in mse_dict_training_list[trial].items(): # only works if there' one min...!!!
        if value == min(mse_dict_training_list[trial].itervalues()): 
            alpha_min_tra = key

    for key, value in mse_dict_validation_list[trial].items(): # only works if there' one min...!!!
        if value == min(mse_dict_validation_list[trial].itervalues()): 
            alpha_min_val = key 
        
    # define yrange for training and validation fitted curves by using coefficients from optimal alphas
    ytraining   = np.polyval(coefficient_dict_training[alpha_min_tra], data1Ax)
    yvalidation = np.polyval(coefficient_dict_training[alpha_min_val], data1Ax) 

    # plot original data with the fitted curve that minimizes the training error, and the curve that minimizes the validation error
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(data1Ax, data1Ay, c = 'black', label = 'data1A')
    ax1.plot(data1Ax, ytraining, c = 'b', label = 'training')
    ax1.plot(data1Ax, yvalidation, c = 'r', label = 'validation')

    # format fig
    plt.title('Trial ' + str(trial + 1))
    plt.ylim(0, 14)
    plt.xlim(-1.5, 1.6)
    plt.legend()
    plt.show()

# determine mean mse over all training_dicts for each alpha
mse_mean_training   = [] # in same order as alpha
mse_mean_validation = [] # in same order as alpha
for item in alpha: # for each alpha value
    mse_list_training   = []
    mse_list_validation = []
    for mse_dict_training in mse_dict_training_list: # go through each training dictionary and pick out that mse that corresponds to alpha
        mse_list_training.append(mse_dict_training[item])
    for mse_dict_validation in mse_dict_validation_list: # go through each validation dictionary and pick out that mse that corresponds to alpha
        mse_list_validation.append(mse_dict_validation[item])
    mse_mean_training.append(mean(mse_list_training)) # append aveage mse for each alpha to mse_mean list
    mse_mean_validation.append(mean(mse_list_validation)) # append aveage mse for each alpha to mse_mean list

# plot fig
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(alpha, mse_mean_training, c = 'b', marker = 'D', label = 'training')
ax1.scatter(alpha, mse_mean_validation, c = 'r', marker = '+', label = 'validation')

# format fig
plt.title('mean MSE of training vs. validation data\nover 20 iterations')
plt.xlabel('alpha')
plt.ylabel('Average Mean Squared Error')
plt.ylim(-0.05, 1)
plt.xlim(0, 13)
plt.legend()
plt.show()
