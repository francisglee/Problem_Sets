# TODO: convert for-loops to list comprehensions
# TODO: Add the rest of the fingerprints

# Let's import SMILES data using Pandas.  How did Messer get through this bug about fragments?  Oh they didn't use rdkit
import pandas as pd
import numpy as np
import time
from rdkit.Chem import AllChem
import rdkit.Chem as Chem
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit import DataStructs	

tic = time.clock()
print time.asctime()

file = "AID2098wSMILES (corrected).csv" # define file that you want to use

original_df = pd.read_csv(file, delimiter = ",")
testing_df  = pd.DataFrame(original_df.loc[0 : 5, "SMILES"])
df          = testing_df

print "size =", df.size, "shape =", df.shape, "indexes =", df.index, "columns =", df.columns # check to make sure the right df proceeds

# TODO: Make this all work in one loop...	
for index, row in df.iterrows():
    
    if index % 10000 == 0: # spot check on terminal
    	print "We're currently processing index", index, time.asctime()

    # check for bugs in SMILES
    if row["SMILES"].find('.') != -1: # returns -1 if no counterions are found 
        df.loc[index, "pSMILES"] = df.loc[index, "SMILES"]
    else:
        df.loc[index, "pSMILES"] = row["SMILES"].split(".")[0]

    df.loc[index, "mol"]         = Chem.MolFromSmiles(df.loc[index, "pSMILES"]) 
    df.loc[index, "ECFP-2"]      = AllChem.GetMorganFingerprint(df.loc[index, "mol"], 2) # radius of 2
    # df.loc[index, "ECFPbvs-2"]   = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 2, nBits = 1024).ToBitString() # radius of 2
    # df.loc[index, "Daylight"] = FingerprintMols.FingerprintMol(df.loc[index, "mol"])

print "size =", df.size, "shape =", df.shape, "indexes =", df.index, "columns =", df.columns # check to make sure the right df proceeds

# let's export this data as a CSV
df.to_csv('SMILEStoFingerprints_ECFP-2.csv')

tock = time.clock()
print time.asctime()
print "Run time for Preprocessing (hr): ", (tock - tic)/60

# compute distance matrix for every Fingerprint type in df
columns       = list(df.index)
indexes       = list(df.index)
# print columns, indexes
# dist_mat_dict = {}
# df['previous_year'] = [row-1 for row in df['year']]

dist_mat = pd.DataFrame(index = indexes, columns = columns) # filled with Nans
# print dist_mat

for index, row in dist_mat.iterrows(): # for each for

	if index % 10000 == 0: # spot check on terminal
    	print "DataMATRIX: We're currently processing index", index, time.asctime()

    counter = 0 # compute only half table

	# print "I am here:", index, row
	for item in columns:		
		if item < counter:
			continue
		else:
			# print "for row", index, "and column", item
			# print " and now i'm here:", df.loc[index, 'ECFP-2'], df.loc[item, 'ECFP-2']
			dist_mat.loc[index, item] = DataStructs.TanimotoSimilarity(df.loc[index, 'ECFP-2'], df.loc[item, 'ECFP-2'])
		counter += 1

# lets export distance matrix
dist_mat.to_csv('Tanimoto_Distance_matrix_ECFP-2.csv')




