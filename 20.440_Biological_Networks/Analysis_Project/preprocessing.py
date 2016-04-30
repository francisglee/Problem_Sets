# Let's import SMILES data using Pandas.  How did Messer get through this bug about fragments?  Oh they didn't use rdkit
import pandas as pd
import numpy as np
import time

tic = time.clock()
print(time.asctime())

file = "AID2098wSMILES (corrected).csv" # define file that you want to use

dataset_df     = pd.read_csv(file, delimiter = ",")
SMILES_df      = pd.DataFrame(dataset_df.loc[ : , "SMILES"]) # All the SMILES, creates a series
SMILES_test_df = pd.DataFrame(dataset_df.loc[0: 100000, "SMILES"]) # try a small subset of 1000
df             = SMILES_test_df

print "original data size, shape, indexes, columns: ", dataset_df.size, dataset_df.shape, dataset_df.index, dataset_df.columns
print "SMILES size, shape, indexes, columns: ", SMILES_df.size, SMILES_df.shape, SMILES_df.index, SMILES_df.columns
print "SMILES_sample size, shape, indexes, columns: ", SMILES_test_df.size, SMILES_test_df.shape, SMILES_test_df.index, SMILES_test_df.columns 
print "size, shape, indexes, columns: ", df.size, df.shape, df.index, df.columns # check to make sure the right df proceeds
# for row in df.itertuples():
#     print row

#####################
# Pre-process SMILES
# - counterions 
# http://rdkit.blogspot.ch/2016/04/revisiting-similarity-comparison-set.html

# TODO:
# - unifying aromaticity models
# - neutralization
# see 'Prediction of Compounds Activity in Nuclear Receptor Signaling and Stress Pathway Assays Using Machine Learning Algorithms and Low-Dimensional Molecular Descriptors'
#####################

# create a new column in SMIILES.df called pSMILES
dfLength = len(df.index)
print "dfLength: ", dfLength

df["pSMILES"] = pd.Series(np.zeros(dfLength), index = df.index)
print "size, shape, indexes, columns: ", df.size, df.shape, df.index, df.columns # check to make sure the right df proceeds

# check for bugs in SMILES
for index, row in df.iterrows():
    if -1 == row["SMILES"].find('.'): # returns -1 if no counterions are found 
        df.loc[index, "pSMILES"] = df.loc[index, "SMILES"]
    else:
        df.loc[index, "pSMILES"] = row["SMILES"].split(".")[0]

# for row in df.itertuples():
#     print row      

#######################################

import rdkit.Chem as Chem

# create a new column in SMIILES.df called mols
df["mol"] = pd.Series(np.zeros(dfLength), index = df.index)
print df.size, df.shape, df.index, df.columns # check to make sure the right df proceeds

# populate mol with data
for index, row in df.iterrows():
    df.loc[index, "mol"] = Chem.MolFromSmiles(df.loc[index, "pSMILES"])
    
# check mol values
# for index, row in df.iterrows():
#     print row, Chem.MolToMolBlock(row["mol"]) 

########################################

#  Let's start with ECFP (Morgans)
from rdkit.Chem import AllChem

# let's define the params
radius = [2, 3, 4]

# create new columns for each ECFP variant
# TODO - can this be looped?
df["ECFP-2"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 2
df["ECFP-3"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 3
df["ECFP-4"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 4
df["ECFPbv-2"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 2
df["ECFPbv-3"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 3
df["ECFPbv-4"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 4
df["ECFPbvs-2"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 2
df["ECFPbvs-3"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 3
df["ECFPbvs-4"] = pd.Series(np.zeros(dfLength), index = df.index) # radius of 4

# check values
print df.size, df.shape, df.index, df.columns # check to make sure the right df proceeds
# for row in df.itertuples():
#     print row

# populate mol with data
for index, row in df.iterrows():
    df.loc[index, "ECFP-2"] = AllChem.GetMorganFingerprint(df.loc[index, "mol"], 2)
    df.loc[index, "ECFP-3"] = AllChem.GetMorganFingerprint(df.loc[index, "mol"], 3)
    df.loc[index, "ECFP-4"] = AllChem.GetMorganFingerprint(df.loc[index, "mol"], 4)
    # df.loc[index, "ECFPbv-2"] = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 2)
    # df.loc[index, "ECFPbv-3"] = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 3)
    # df.loc[index, "ECFPbv-4"] = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 4)
    df.loc[index, "ECFPbvs-2"] = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 2, nBits = 1024).ToBitString()
    df.loc[index, "ECFPbvs-3"] = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 3, nBits = 1024).ToBitString()
    df.loc[index, "ECFPbvs-4"] = AllChem.GetMorganFingerprintAsBitVect(df.loc[index, "mol"], 4, nBits = 1024).ToBitString()

# check values
print df.size, df.shape, df.index, df.columns # check to make sure the right df proceeds
# for row in df.itertuples():
#     print row 

# let's export this data as a CSV
df.to_csv('SMILEStoFingerprints.csv')

tock = time.clock()
print "Run time: ", tock - tic
